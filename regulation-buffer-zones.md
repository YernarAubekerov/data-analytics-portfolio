# 📋 Regulation: Shipment via Buffer Zones P02–P11

> **Document type:** Operational Regulation  
> **Version:** 1.0  
> **Date:** 30 May 2024  
> **Status:** Active

---

## Purpose / Назначение

This regulation defines the step-by-step procedure for staging warehouse pallets in buffer zones (cells P02–P11) prior to shipment, ensuring correct dock assignment and clear WMS task management.

---

## Scope / Область применения

Applies to all shipment operations involving pallet delivery to dispatch docks via buffer staging zones.

---

## Key Principle / Ключевой принцип

> **Buffer cell number = Dock number**  
> Buffer cell P05 serves exclusively Dock 5. There are no exceptions.

---

## Process Steps / Шаги процесса

### Step 1 — Dock Assignment
**Actor:** Coordinator  
**Action:** Informs the forklift driver which dock to prepare pallets for.  
**Output:** Driver knows target dock number.

### Step 2 — Pallet Movement to Buffer
**Actor:** Forklift Driver (Storage)  
**Action:** Moves required pallets from storage cell to the corresponding buffer cell using the WMS **"Movement" (Перемещение)** operation.  
**Rule:** Target cell = P0[Dock Number] (e.g., Dock 7 → Cell P07)  
**Output:** Pallets physically in buffer cell; WMS records movement.

### Step 3 — Pick Task Creation
**Actor:** WMS Operator  
**Action:** Creates a **Pick Task (Задание на Отбор)** from the buffer cell, specifying the same dock number.  
**Output:** Pick task created in WMS with correct dock reference.

### Step 4 — Pick Execution
**Actor:** Forklift Driver (Dispatch)  
**Action:** Picks all pallets from the buffer cell and loads them at the assigned dock. Reports completion to WMS Operator.  
**Output:** All pallets loaded; dock ready for dispatch.

### Step 5 — Status Update
**Actor:** WMS Operator  
**Action:** Updates the Pick Task status from **"In Pick"** to **"Ready for Dispatch" (К Отгрузке)**.  
**Note:** Automatic status transition planned for future WMS version.  
**Output:** Task closed; shipment ready.

---

## Responsibility Matrix (RACI)

| Step | Coordinator | Driver (Storage) | WMS Operator | Driver (Dispatch) |
|------|:-----------:|:----------------:|:------------:|:-----------------:|
| Dock assignment | **R** | I | I | — |
| Pallet movement | I | **R** | C | — |
| Pick task creation | — | — | **R** | I |
| Pick execution | — | — | I | **R** |
| Status update | — | — | **R** | C |

*R = Responsible | C = Consulted | I = Informed*

---

## Buffer Cell Map / Карта буферных ячеек

```
Dock:    02    03    04    05    06    07    08    09    10    11
         │     │     │     │     │     │     │     │     │     │
Buffer:  P02   P03   P04   P05   P06   P07   P08   P09   P10   P11
```

---

## Error Handling / Обработка ошибок

| Situation | Action |
|-----------|--------|
| Pallets moved to wrong buffer cell | Driver reverses movement; Coordinator reassigns |
| Buffer cell occupied by other pallets | WMS Operator checks open tasks; Coordinator decides |
| Pick task created for wrong dock | WMS Operator cancels and recreates with correct dock |

---

*← [Back to WMS Project](../README.md) | [Back to Portfolio](../../README.md)*
