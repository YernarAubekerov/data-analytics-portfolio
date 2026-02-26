# 📊 Data & Business Analytics Portfolio

> **[RU]** Портфолио аналитика данных | **[EN]** Data Analyst Portfolio  
> _Logistics & Supply Chain Domain | WMS · CTMS · KPI · Process Optimization_

---

## 👋 About Me / О себе

**[EN]** I am a business analyst transitioning into data analytics, with hands-on experience in logistics operations — warehouse management systems (WMS), container terminal management (CTMS), and KPI reporting. I combine deep domain knowledge with analytical tools to turn operational data into actionable insights.

**[RU]** Аналитик с опытом в логистике и управлении складом (WMS), контейнерными терминалами (CTMS) и KPI-отчётностью. Моя цель — перейти в роль Data Analyst, объединяя знание бизнес-процессов с аналитическими инструментами.

---

## 🗂️ Projects / Проекты

| # | Project | Domain | Tools | Language |
|---|---------|--------|-------|----------|
| 1 | [📦 CTMS — Container Terminal Analytics](#1--ctms--container-terminal-analytics) | Logistics / Container Terminal | Excel, Power BI | RU/EN |
| 2 | [🏭 WMS — Warehouse Process Optimization](#2--wms--warehouse-process-optimization) | Warehouse Management | Excel, Power Query | RU/EN |
| 3 | [📈 KPI Dashboard — Train Loading Control](#3--kpi-dashboard--train-loading-control) | Operations / KPI | Excel, Power BI | RU/EN |

---

## 1. 📦 CTMS — Container Terminal Analytics

📁 [`/ctms-analysis`](./ctms-analysis/)

### What was done / Что сделано
**[EN]**  
Participated in the business requirements analysis and process documentation for the **CTMS** system (Container Terminal Management System built on 1C:Enterprise 8.3). Mapped end-to-end container flows, identified gaps in current operations, and described key operational workflows.

**[RU]**  
Участвовал в анализе бизнес-требований и документировании процессов для системы **CTMS** (Система управления контейнерным терминалом на базе 1С:Предприятие 8.3). Описал сквозные потоки контейнеров, выявил узкие места и задокументировал ключевые операции.

### Key Activities / Ключевые действия
- 🔍 Mapped container lifecycle: **Arrival → Inspection → Storage → Loading → Dispatch**
- 📋 Documented business processes for 3 terminal zones (Reception, Storage, Dispatch)
- 📊 Analyzed container types (TEU/FEU), ISO codes, and weight characteristics
- ⚠️ Identified process bottlenecks and proposed system improvements
- 🔗 Described integrations: Railway system ↔ CTMS ↔ WMS ↔ Loading equipment

### Results / Результаты
| Metric | Value |
|--------|-------|
| Processes documented | 6 core operations |
| Container types analyzed | TEU (20ft) + FEU (40ft) |
| System integrations mapped | 3 (Railway, WMS, Equipment) |
| Damage types classified | 8+ categories |

### Tools / Инструменты
`1C:Enterprise 8.3` · `Excel` · `Power BI` · `Business Process Modeling`

---

## 2. 🏭 WMS — Warehouse Process Optimization

📁 [`/warehouse-optimization`](./warehouse-optimization/)

### What was done / Что сделано
**[EN]**  
Analyzed and optimized the **shipment via buffer zones** process in a WMS (Warehouse Management System). Identified inefficiencies in pallet movement between storage cells and dispatch docks. Developed and documented a new operational regulation that reduced idle time and improved dock coordination.

**[RU]**  
Проанализировал и оптимизировал процесс **отгрузки через буферные ячейки** в системе WMS. Выявил неэффективность в перемещении паллет между ячейками хранения и доками отгрузки. Разработал и задокументировал новый операционный регламент, сократив простои и улучшив координацию доков.

### Problem → Solution / Проблема → Решение

```
BEFORE (AS-IS):
Coordinator → Forklift Driver → Storage Cell → Dock
❌ No buffer system → Multiple trips → Dock idle time

AFTER (TO-BE):
Coordinator → Forklift Driver → Buffer Cell P02-P11 → Dock
✅ Buffer zones matched to dock numbers
✅ WMS operator creates pick tasks from buffer
✅ Clear status flow: "In Pick" → "Ready for Dispatch"
```

### Process Flow / Схема процесса
```
1. Coordinator assigns dock number
2. Driver moves pallets: Storage Cell → Buffer Cell (P02–P11)
   └─ Cell number = Dock number (clear 1:1 mapping)
3. WMS Operator creates Pick Task from buffer cell
4. Driver completes pick & reports to WMS Operator  
5. WMS Operator updates status → "Ready for Dispatch"
```

### Results / Результаты
- ✅ Eliminated dock confusion through 1:1 cell-to-dock mapping
- ✅ Reduced forklift idle trips via structured buffer staging
- ✅ Clear accountability chain (Coordinator → Driver → WMS Operator)
- ✅ Potential for automatic status transitions in WMS

### Tools / Инструменты
`WMS System` · `Excel` · `Process Mapping` · `Regulation Writing`

---

## 3. 📈 KPI Dashboard — Train Loading Control

📁 [`/kpi-dashboard`](./kpi-dashboard/)

### What was done / Что сделано
**[EN]**  
Built and maintained KPI tracking models in Excel for monitoring train loading operations. Analyzed daily loading performance against plan, tracked deviations, and prepared operational reports for management.

**[RU]**  
Разработал и поддерживал KPI-модели в Excel для мониторинга операций по загрузке поездов. Анализировал фактическое выполнение плана погрузки, отслеживал отклонения и готовил оперативные отчёты для руководства.

### Key Metrics Tracked / Ключевые показатели
| KPI | Description |
|-----|-------------|
| Train loading plan vs. actual | Percentage completion per shift/day |
| Container throughput | TEU processed per day |
| Dock utilization | % of available dock time used |
| Deviation alerts | Flagging underperformance > threshold |

### Tools / Инструменты
`Excel` · `Power Query` · `Power BI` · `KPI Modeling`

---

## 🛠️ Skills & Tools / Навыки и инструменты

```
Analytics & Reporting:
  ✦ Excel (Advanced) — PivotTables, Power Query, formulas, dashboards
  ✦ Power BI — data modeling, DAX, interactive dashboards

Domain Knowledge:
  ✦ WMS (Warehouse Management Systems)
  ✦ CTMS (Container Terminal Management)
  ✦ KPI design and tracking
  ✦ Business process mapping and documentation
  ✦ Operational reporting

Soft Skills:
  ✦ Requirements gathering and stakeholder communication
  ✦ Process analysis (AS-IS / TO-BE)
  ✦ Regulation and SOP writing
  ✦ Cross-functional coordination (IT, Operations, Management)
```

---

## 📬 Contact / Контакты

> Replace with your actual contacts below

- 📧 Email: `yernaraubekerov@gmail.com`
- 💼 LinkedIn: `www.linkedin.com/in/yernar-aubekerov-204683387`
- 📍 Location: Kazakhstan / Remote

---

## 📁 Repository Structure / Структура репозитория

```
portfolio/
├── README.md                          ← You are here
├── ctms-analysis/
│   ├── README.md                      ← Project deep-dive
│   ├── process-map.md                 ← Container lifecycle mapping
│   └── business-requirements.md      ← Key requirements & gaps
├── warehouse-optimization/
│   ├── README.md                      ← Project deep-dive
│   ├── as-is-process.md               ← Current state analysis
│   ├── to-be-process.md               ← Optimized process
│   └── regulation-buffer-zones.md    ← Final operational regulation
├── kpi-dashboard/
│   ├── README.md                      ← Project deep-dive
│   └── kpi-model-description.md      ← Metrics & logic explained
└── docs/
    └── logistics-glossary.md          ← Domain terms reference
```

---

*Last updated: 2024 | Open to Data Analyst opportunities*
