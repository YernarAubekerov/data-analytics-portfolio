# 📈 Project 3: KPI Dashboard — Train Loading Control

[![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://office.com)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)](https://powerbi.microsoft.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

> **Domain:** Operations Management / KPI Reporting  
> **Role:** Data Analyst / Reporting Analyst  
> **Tools:** Excel · Power Query · Power BI  
> **Date:** 2023–2024

---

## 🎯 Project Goal / Цель проекта

**[EN]** Design and maintain a KPI tracking system to monitor daily train loading operations against plan, identify deviations in real-time, and provide management with actionable operational reports.

**[RU]** Разработать и поддерживать систему отслеживания KPI для мониторинга ежедневных операций погрузки поездов, выявления отклонений в реальном времени и предоставления руководству оперативных отчётов.

---

## 📊 KPI Framework / Система показателей

See the [KPI Model Description](./kpi-model-description.md) for detailed formulas and workbook architecture.

---

## 💡 Key Excel Formulas Used / Ключевые формулы

```excel
-- Plan Completion Percentage
=IFERROR([@[Actual_TEU]]/[@[Plan_TEU]]*100, 0)

-- Deviation Alert Flag (conditional)  
=IF([@[Completion_%]]<80, "🔴 CRITICAL",
  IF([@[Completion_%]]<95, "🟡 WARNING", "🟢 OK"))

-- 7-day Rolling Average
=AVERAGEIFS(KPI[Completion_%], KPI[Date], ">="&(TODAY()-7))

-- YTD Cumulative TEU
=SUMPRODUCT((YEAR(KPI[Date])=YEAR(TODAY()))*KPI[Actual_TEU])
```

---

## 📈 Power Query Transformations / Трансформации Power Query

```
Step 1: Load raw CSV/Excel data from operational system
Step 2: Remove nulls and standardize date formats
Step 3: Merge with train schedule reference table
Step 4: Calculate derived columns:
         - Completion % = Actual / Plan
         - Variance = Actual - Plan  
         - Status = SWITCH on completion %
Step 5: Group by week/month for trend analysis
Step 6: Output to KPI_SUMMARY table
```

---

## 📊 Power BI Dashboard Design / Дизайн дашборда

### Page 1: Executive Summary / Руководство
```
┌──────────────────────────────────────────────────────┐
│           Train Loading KPI — August 2024            │
├─────────┬─────────┬─────────┬────────────────────────┤
│  95.2%  │  1,847  │  88.4%  │  3 trains late         │
│  Plan   │TEU This │  Dock   │  this week             │
│Compltn. │  Month  │  Util.  │                        │
├─────────┴─────────┴─────────┴────────────────────────┤
│  Daily TEU Trend (Line) vs. Plan (dotted)           │
│  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              │
├─────────────────────────────┬────────────────────────┤
│  By Train: Completion %     │  Deviation Heatmap     │
│  (Bar chart, sorted desc.)  │  (Calendar view)       │
└─────────────────────────────┴────────────────────────┘
```

### Page 2: Operational Detail / Операционная детализация
```
┌──────────────────────────────────────────────────────┐
│  Drill-down by Train Number / Date / Dock            │
├──────────────────────────────────────────────────────┤
│  Table: Train-level KPIs with conditional formatting │
│  ┌──────────┬────────┬────────┬──────────┬────────┐ │
│  │ Train    │ Plan   │ Actual │    %     │ Status │ │
│  ├──────────┼────────┼────────┼──────────┼────────┤ │
│  │24/52 OOC │   62   │   62   │  100%    │  🟢   │ │
│  │24/51 REI │   58   │   47   │   81%    │  🔴   │ │
│  └──────────┴────────┴────────┴──────────┴────────┘ │
└──────────────────────────────────────────────────────┘
```

---

## 🐍 Live KPI Analysis / Живой анализ KPI

We have implemented a Python script to generate real-time KPI reports from operational data.

**Run the report:**
```bash
python3 generate_kpi_report.py
```

## 🔍 Insights Generated / Полученные инсайты

### Example Findings from Analysis / Примеры выводов

1. **Peak underperformance on Mondays** — loading completion averaged 82% vs. 95%+ rest of week
   - *Root cause:* Weekend equipment maintenance delays start of week
   - *Recommendation:* Move planned maintenance to Friday evening

2. **2 specific train routes consistently underperform** (24/51, 24/39)
   - *Root cause:* Higher share of heavy FEU containers requiring special equipment
   - *Recommendation:* Pre-assign heavy lift equipment for these routes

3. **Dock utilization drops sharply after 17:00**
   - *Root cause:* Shift handover gap — 30-45 min with no active loading
   - *Recommendation:* Stagger shift times by 30 min for continuity

---

## 📋 Reporting Cadence / Периодичность отчётности

| Report | Frequency | Audience | Format |
|--------|-----------|---------|--------|
| Daily Ops Flash | Daily | Operations Manager | Email summary |
| Weekly KPI Review | Weekly | Department Head | Excel + Charts |
| Monthly Performance | Monthly | Senior Management | Power BI PDF |

---

## 📂 Files in This Folder / Файлы в папке

| File | Description |
|------|-------------|
| `README.md` | This file — project overview |
| `kpi-model-description.md` | Detailed KPI definitions and calculation logic |

---

*← [Back to Portfolio](../README.md)*
