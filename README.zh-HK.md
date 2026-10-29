# 香港儀器及監測工程 QS Skills

此版本專門處理 **儀器及監測（I&M）**、**涉及儀器的地質勘探（Ground Investigation）**，以及 **涉及儀器的地基／地質改良（Ground Improvement）** 的工料測量工作。

代理指令使用英文；可要求以繁體中文輸出工程量表、估價、付款評估及招標問題清單。

## 七個技能

| 技能 | 用途 |
|---|---|
| hkqs-general | 確定工作範圍、合約、量度文件版本及證據，分派所需技能 |
| hkqs-instrumentation-monitoring | 整理儀器／監測點、ADMS、基準讀數、監測頻率、服務期及計價單位 |
| hkqs-ground-investigation | 核對鑽孔深度、試驗、儀器安裝及勘探與監測的責任界面 |
| hkqs-ground-improvement | 核對試驗段、處理範圍／體積、重疊、施工次數、驗證及監測配套 |
| hkqs-cost-estimation | 用報價及資源資料組合單價，處理購買／租賃、通訊、平台及延長服務成本 |
| hkqs-valuation-variations | 進度估值、付款證書對數、變更、延長監測及通知證據 |
| hkqs-tender-review | 核對規格、BOQ、報價和責任分工，提出具體 RFI |

## 實際會防止甚麼問題

- 把一套系統的「月費」，錯乘成每台儀器的月費。
- 把每五秒上傳資料，當作每五秒都有一個可另行收費的完整讀數。
- 安裝單價已包括讀數、校準或保養，卻在另一行重複收費。
- 一個鑽孔安裝一支測斜管，再重複計算同一鑽孔長度。
- 把重複處理次數直接乘入「淨改良土體體積」。
- 把已發付款證書、已收現金及本期應估值混為一談。
- 在未確定合約條款及指示前，把全部補做工程或延長監測當作可索償變更。

上述處理均須以項目實際採用的條款、特別量度規則及證據為準；不是固定的收費結論。

## 香港參考文件

以 CEDD 的《Standard Method of Measurement for Civil Engineering Works, 1992 Edition》、GS2020 第7節相關部分、GEO Geoguide 2／3、監測測量指引、相關 GEO 技術文件，以及適用的 GCC／NEC／分包合約為主要路線。

詳見 [18項官方來源登記冊](skills/hkqs-general/references/source-register.json) 及 [量度文件對照](skills/hkqs-general/references/measurement-sources.md)。已核查日期為 **2026年10月29日**；使用時仍須核對項目採用版本及修訂。

## 使用方式

按照 [英文 README 的安裝步驟](README.md#install-from-a-local-checkout)，將七個技能一併安裝；每次只載入核心及相關專項。

可直接要求：

> 幫我審查這份監測分包 tender，列出儀器、鑽孔、基準讀數、監測期、保養及延長服務的漏項與責任界面，並以繁體中文提出 RFI。

> 根據這份合約的量度規則，對數本月鑽孔、測斜管、壓力計安裝及監測記錄，分開顯示原始工程量、可估值工程量及尚欠證據。

## 結果狀態

| 狀態 | 意思 |
|---|---|
| CALCULATION_ONLY | 算式或情境可追溯，但尚未確認合約計價基礎 |
| NEEDS_SOURCE | 指定資料或條款未有／互相矛盾，須補充才能判斷 |
| READY_FOR_QS_REVIEW | 具備來源及計算依據，可交負責 QS 審核；不等於已批准付款 |

工程師仍負責設計、儀器配置是否足夠、警戒／行動值、改良參數及工程驗收。技能不會自行設定這些數值或批准復工。
