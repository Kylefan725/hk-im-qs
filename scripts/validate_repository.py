#!/usr/bin/env python3
"""Validate structure and local references; never claim technical certification."""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'hk-im-qs'}
LEGACY_SKILLS = {
    'hkqs-mode',
    'hkqs-general', 'hkqs-instrumentation-monitoring', 'hkqs-ground-investigation',
    'hkqs-ground-improvement', 'hkqs-cost-estimation', 'hkqs-valuation-variations',
    'hkqs-tender-review',
}
SKILL_PATH = Path('skills/hk-im-qs')
PLAYBOOKS = {
    'review-tender', 'measure-quantities', 'estimate-and-compare-quotes',
    'value-progress', 'assess-change', 'explain-documents',
}
GUIDE_CHECKLISTS = {
    'references/pricing-anomalies.md',
    'references/risk-allowances.md',
    'references/historical-rates.md',
}
REQUIRED_ROUTER_LINKS = {
    *(f'playbooks/{name}.md' for name in PLAYBOOKS),
    *GUIDE_CHECKLISTS,
    'references/embedded-workflow.md',
    'references/guide-provenance.json',
    'references/project-basis.md',
    'references/domains/instrumentation-monitoring.md',
    'references/domains/ground-investigation.md',
    'references/domains/ground-improvement.md',
}
PLAYBOOK_HEADINGS = {'Inputs', 'Steps', 'Outputs', 'Completion checks'}
SOURCE_PREFIX = r'(?:CEDD|GEO|LESB|DEVB|NEC|CSD)-[A-Z0-9-]+'
STATES = {'CALCULATION_ONLY', 'NEEDS_SOURCE', 'READY_FOR_QS_REVIEW'}


def markdown_links(content: str) -> list[str]:
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skill_root = root / SKILL_PATH
    expected_paths = {SKILL_PATH / 'SKILL.md'}
    actual_paths = {p.relative_to(root) for p in (root/'skills').rglob('SKILL.md')}
    if actual_paths != expected_paths:
        missing = sorted(str(p) for p in expected_paths - actual_paths)
        extra = sorted(str(p) for p in actual_paths - expected_paths)
        errors.append(f'Exactly one entry skill required: missing={missing}, extra={extra}')
    for name in sorted(EXPECTED):
        path = root / 'skills' / name / 'SKILL.md'
        if not path.is_file():
            continue
        content = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
        if not match:
            errors.append(f'{name}: missing frontmatter')
            continue
        fields = {}
        for line in match.group(1).splitlines():
            key, separator, value = line.partition(':')
            if not separator or not value.strip():
                errors.append(f'{name}: invalid one-line frontmatter field')
            fields[key] = value.strip()
        if set(fields) != {'name', 'description'} or fields.get('name') != name:
            errors.append(f'{name}: frontmatter name/fields mismatch')
        if len(name) > 64 or not re.fullmatch(r'[a-z0-9-]+', name):
            errors.append(f'{name}: invalid skill name')
        if len(content.splitlines()) > 500:
            errors.append(f'{name}: exceeds 500-line skill limit')
        router_links = {unquote(link.split('#', 1)[0]) for link in markdown_links(content)}
        for link in sorted(REQUIRED_ROUTER_LINKS - router_links):
            errors.append(f'{name}: missing router link {link}')
        for state in STATES:
            if state not in content:
                errors.append(f'{name}: missing status {state}')

    actual_playbooks = {p.stem for p in (skill_root/'playbooks').glob('*.md')}
    if actual_playbooks != PLAYBOOKS:
        errors.append('Playbook set mismatch: '
                      f'missing={sorted(PLAYBOOKS-actual_playbooks)}, '
                      f'extra={sorted(actual_playbooks-PLAYBOOKS)}')
    for name in sorted(PLAYBOOKS & actual_playbooks):
        content = (skill_root/'playbooks'/f'{name}.md').read_text(encoding='utf-8')
        headings = set(re.findall(r'^## (.+?)\s*$', content, re.M))
        for heading in sorted(PLAYBOOK_HEADINGS - headings):
            errors.append(f'{name}: missing playbook heading {heading}')
    if not (skill_root/'references/valuation-rules.md').is_file():
        errors.append('Missing shared valuation rules')

    registry_path = skill_root / 'references/source-register.json'
    try:
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
        entries = registry['sources']
        ids = {entry['id'] for entry in entries}
        if len(ids) != len(entries):
            errors.append('Duplicate source IDs')
        for entry in entries:
            for key in ('id', 'title', 'publisher', 'edition_or_series', 'official_url',
                        'access', 'verification_level', 'verified_on', 'applicability_caveat'):
                if not entry.get(key):
                    errors.append(f'{entry.get("id", "unknown")}: missing {key}')
            dt.date.fromisoformat(entry['verified_on'])
            if entry['verification_level'] not in registry['evidence_levels']:
                errors.append(f'{entry["id"]}: unknown evidence level')
            for url in [entry['official_url'], *entry.get('related_urls', [])]:
                if urlsplit(url).scheme != 'https' or not urlsplit(url).netloc:
                    errors.append(f'{entry["id"]}: invalid HTTPS reference')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid source register: {exc}')
        ids = set()

    provenance_path = skill_root / 'references/guide-provenance.json'
    try:
        provenance = json.loads(provenance_path.read_text(encoding='utf-8'))
        repository = provenance['repository']
        revision = provenance['revision']
        if repository != 'https://github.com/Kylefan725/qs-skills-guide':
            errors.append('Guide provenance: unexpected repository')
        if not re.fullmatch(r'[0-9a-f]{40}', revision):
            errors.append('Guide provenance: revision must be an immutable commit')
        dt.date.fromisoformat(provenance['reviewed_on'])
        if provenance['authority'] != 'secondary_training_guidance':
            errors.append('Guide provenance: invalid authority')
        checklists = provenance['checklists']
        paths = [entry['path'] for entry in checklists]
        if set(paths) != GUIDE_CHECKLISTS or len(paths) != len(GUIDE_CHECKLISTS):
            errors.append('Guide provenance: checklist set mismatch')
        for entry in checklists:
            path = (skill_root / entry['path']).resolve()
            if not path.is_relative_to(skill_root.resolve()) or not path.is_file():
                errors.append(f'Guide provenance: missing bundled checklist {entry["path"]}')
            source_url = entry['source_url']
            pinned_path = re.escape(f'{repository}/blob/{revision}/guides/')
            if not isinstance(source_url, str) or not re.fullmatch(
                    pinned_path + r'(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]+\.md', source_url):
                errors.append(f'Guide provenance: source URL is not pinned for {entry["path"]}')
            sections = entry['reviewed_sections']
            if not isinstance(sections, list) or not sections or not all(
                    isinstance(section, str) and section.strip() for section in sections):
                errors.append(f'Guide provenance: missing reviewed sections for {entry["path"]}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid guide provenance: {exc}')

    markdown = [root/'README.md', root/'README.zh-HK.md',
                *(root/'docs').glob('*.md'), *(root/'skills').rglob('*.md')]
    for path in markdown:
        if not path.is_file():
            errors.append(f'Missing document: {path.relative_to(root)}')
            continue
        content = path.read_text(encoding='utf-8')
        for target in markdown_links(content):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            local_target = unquote(target.split('#', 1)[0])
            resolved = (path.parent / local_target).resolve()
            parts = Path(local_target).parts
            if any(name in parts for name in LEGACY_SKILLS) and parts[-1:] == ('SKILL.md',):
                errors.append(f'{path.relative_to(root)}: legacy skill link {target}')
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f'{path.relative_to(root)}: broken local link {target}')
            elif path.is_relative_to(skill_root) and not resolved.is_relative_to(skill_root.resolve()):
                errors.append(f'{path.relative_to(root)}: link leaves the installable skill {target}')
        for source_id in set(re.findall(r'`(' + SOURCE_PREFIX + r')`', content)):
            if source_id not in ids:
                errors.append(f'{path.relative_to(root)}: unknown source ID {source_id}')
    for file in (root/'skills').rglob('*'):
        if file.is_file() and file.suffix.lower() in {'.pdf', '.docx', '.xlsx', '.zip'}:
            errors.append(f'Unexpected source/binary in skills: {file.relative_to(root)}')
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print('\n'.join('ERROR: '+item for item in errors))
        return 1
    registry = json.loads((ROOT/SKILL_PATH/'references/source-register.json').read_text())
    print(f'PASS: {len(EXPECTED)} entry skill, {len(PLAYBOOKS)} playbooks, '
          f'{len(registry["sources"])} source entries, frontmatter, '
          f'{len(GUIDE_CHECKLISTS)} pinned guide checklists, '
          'self-contained links and evidence references')
    print('Structural validation only; source applicability and professional decisions require review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
