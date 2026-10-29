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
EXPECTED = {
    'hkqs-general', 'hkqs-instrumentation-monitoring', 'hkqs-ground-investigation',
    'hkqs-ground-improvement', 'hkqs-cost-estimation', 'hkqs-valuation-variations',
    'hkqs-tender-review',
}
SOURCE_PREFIX = r'(?:CEDD|GEO|LESB|DEVB|NEC|CSD)-[A-Z0-9-]+'
STATES = {'CALCULATION_ONLY', 'NEEDS_SOURCE', 'READY_FOR_QS_REVIEW'}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    actual = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    if actual != EXPECTED:
        errors.append(f'Skill set mismatch: missing={sorted(EXPECTED-actual)}, extra={sorted(actual-EXPECTED)}')
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
        if name != 'hkqs-general' and '../hkqs-general/SKILL.md' not in content:
            errors.append(f'{name}: missing core dependency')
        for state in STATES:
            if state not in content:
                errors.append(f'{name}: missing status {state}')

    registry_path = root / 'skills/hkqs-general/references/source-register.json'
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

    markdown = [root/'README.md', root/'README.zh-HK.md',
                *(root/'docs').glob('*.md'), *(root/'skills').rglob('*.md')]
    for path in markdown:
        if not path.is_file():
            errors.append(f'Missing document: {path.relative_to(root)}')
            continue
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            resolved = (path.parent / unquote(target.split('#', 1)[0])).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f'{path.relative_to(root)}: broken local link {target}')
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
    registry = json.loads((ROOT/'skills/hkqs-general/references/source-register.json').read_text())
    print(f'PASS: {len(EXPECTED)} skills, {len(registry["sources"])} source entries, frontmatter, local links and evidence references')
    print('Structural validation only; source applicability and professional decisions require review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
