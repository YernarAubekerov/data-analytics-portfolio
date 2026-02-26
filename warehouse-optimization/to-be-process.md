# ✅ TO-BE Process Design

## Optimized Process Flow

**Key Design Decision:** Buffer cells P02–P11 are numbered to **match dock numbers exactly** (Buffer P05 = Dock 5).

### Step-by-Step Procedure

1. **STEP 1: Coordinator assigns dock number to Driver**
2. **STEP 2: Driver picks pallets & moves to Buffer Cell**
   - Storage Cell ──────→ Buffer Cell P0X (matches Dock X)
3. **STEP 3: WMS Operator creates Pick Task**
   - Buffer Cell P0X → Pick Task (same dock number)
4. **STEP 4: Assigned Driver completes pick**
   - Picks all pallets from buffer → Loads dock
   - Reports completion to WMS Operator
5. **STEP 5: WMS Operator updates status**
   - "In Pick" ──────→ "Ready for Dispatch"

*← [Back to WMS Project](./README.md)*
