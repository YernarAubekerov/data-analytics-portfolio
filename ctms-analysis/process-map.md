# 🔄 Container Lifecycle Mapping

## Lifecycle Steps

```
ARRIVAL (Прибытие)
    │
    ▼
EXPECTED RECEIPT (Ожидаемое поступление)
    │  └─ Train arrives at station
    │  └─ Receipt application created
    │  └─ Train dispatched to front
    │
    ▼
INSPECTION (Осмотр)
    │  └─ External inspection before unloading
    │  └─ Damage assessment (8+ damage types)
    │  └─ Criteria: Sealing · Odor · Cleanliness · Seaworthiness
    │
    ▼
UNLOADING & PLACEMENT (Выгрузка и размещение)
    │  └─ Containers unloaded from platforms
    │  └─ Internal inspection
    │  └─ Moved to storage zone
    │
    ▼
STORAGE (Хранение)
    │  └─ Positioned in terminal topology
    │  └─ Cell system: Zone → Section → Row → Tier
    │
    ▼
[OPTIONAL] STUFFING / LOADING (Затарка)
    │  └─ Stuffing request → Assembly task
    │  └─ Container delivered to warehouse
    │  └─ Goods loaded
    │
    ▼
DISPATCH (Отгрузка)
       └─ Shipment order created
       └─ Platform request submitted
       └─ Platform inspection
       └─ Loading
       └─ Transfer to Railway carrier
       └─ Train departure
       └─ Loading info transmitted
```

*← [Back to CTMS Project](./README.md)*
