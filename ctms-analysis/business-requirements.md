# 🔍 CTMS Business Requirements & Gaps

## Identified Gaps / Выявленные пробелы
1. **Missing mandatory fields** — "Train" field not always populated in container receipts
2. **N/A container types** — Many containers arrive with unclassified type; requires classification improvement
3. **Manual status transitions** — Some statuses require manual update; automation recommended
4. **Topology underutilization** — Cell assignment not always optimized for turnaround speed

## Recommendations / Рекомендации
| Priority | Issue | Recommendation |
|----------|-------|---------------|
| 🔴 High | Missing Train field | Make mandatory in receipt form |
| 🔴 High | N/A container types | Pre-populate from carrier manifests |
| 🟡 Medium | Manual status updates | Automate "In Pick → Ready for Dispatch" |
| 🟡 Medium | Topology planning | Implement placement algorithm by dispatch date |
| 🟢 Low | Reporting | Add TEU throughput dashboard |

*← [Back to CTMS Project](./README.md)*
