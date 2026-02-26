# 📊 KPI Model Description

## KPI Framework

| KPI | Formula | Target | Alert |
|-----|---------|--------|-------|
| **Plan Completion %** | Actual TEU / Plan TEU × 100 | ≥ 95% | < 80% 🔴 |
| **Daily Container Throughput** | Sum of TEU dispatched per day | Per plan | -10% 🟡 |
| **Dock Utilization Rate** | Active dock hours / Total dock hours | ≥ 85% | < 70% 🔴 |
| **Train Departure Compliance** | On-time departures / Total departures | ≥ 90% | < 75% 🔴 |

## Excel Model Architecture

```
Workbook Structure:
│
├── RAW_DATA sheet
│   └─ Daily input: date, train, containers planned/actual, dock, status
│
├── POWER_QUERY transformations
│   ├─ Clean and normalize raw data
│   ├─ Calculate daily KPIs
│   └─ Flag deviations automatically
│
├── KPI_SUMMARY sheet
│   ├─ Current period performance
│   ├─ Rolling 7-day and 30-day trends
│   └─ Deviation alerts table
│
└── DASHBOARD sheet
    ├─ Visual KPI cards (Plan vs. Actual)
    ├─ Trend line charts
    └─ Red/Yellow/Green status indicators
```

*← [Back to KPI Project](./README.md)*
