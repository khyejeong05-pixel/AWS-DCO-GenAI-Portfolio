# 📊 AWS DCO 교육용 샘플 로그 분석 결과 보고서
**생성 시간**: 2026-07-19

---
## 1. 📈 전체 로그 요약
- **전체 로그 라인 수**: 140개

## 2. 🛡️ 심각도별 분포
| 심각도 (Severity) | 개수 (Count) | 비율 (Percentage) |
| --- | --- | --- |
| `INFO` | 135개 | 96.4% |
| `WARNING` | 3개 | 2.1% |
| `ERROR` | 2개 | 1.4% |

## 3. 🏷️ 주요 이벤트 발생 빈도 Top 10
| 순위 | 이벤트명 (Event) | 발생 개수 | 비율 |
| --- | --- | --- | --- |
| 1 | Normal heartbeat | 125개 | 89.3% |
| 2 | Ticket opened | 3개 | 2.1% |
| 3 | Ticket escalated | 3개 | 2.1% |
| 4 | Maintenance completed | 3개 | 2.1% |
| 5 | Fan Alert | 1개 | 0.7% |
| 6 | Temperature warning | 1개 | 0.7% |
| 7 | SSD failure warning | 1개 | 0.7% |
| 8 | CRC error 증가 | 1개 | 0.7% |
| 9 | Link Down | 1개 | 0.7% |
| 10 | Link Up | 1개 | 0.7% |

## 4. ⚠️ 주의 및 경고 로그 목록 (WARNING / ERROR / CRITICAL)
| 시간 | 장비명 (Device) | 심각도 | 이벤트 | 상세 내용 |
| --- | --- | --- | --- | --- |
| 2026-07-03 01:05:00 | `DEMO_CORE_SW_02` | **WARNING** | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | `EDU_SRV_R04_N12` | **WARNING** | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 02:10:00 | `EDU_SRV_R04_N12` | **ERROR** | SSD failure warning | Drive Slot 3 SSD wearout indicator FAILING (SMART wear 96%). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | `SAMPLE_TOR_SW_01` | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| 2026-07-03 03:06:00 | `SAMPLE_TOR_SW_01` | **ERROR** | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |

## 5. 🔍 핵심 장애 및 운영 관리 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)
데이터 센터 네트워크 인프라 및 티켓 관리에서 추적이 필요한 핵심 이벤트 항목입니다.
| 시간 | 장비명 (Device) | 감지 분류 (Category) | 이벤트 | 상세 내용 |
| --- | --- | --- | --- | --- |
| 2026-07-03 01:10:00 | `DEMO_CORE_SW_02` | <span style='color:red'>**TICKET_ESCALATED**</span> | Ticket escalated | Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team. |
| 2026-07-03 02:15:00 | `EDU_SRV_R04_N12` | <span style='color:red'>**TICKET_ESCALATED**</span> | Ticket escalated | Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support. |
| 2026-07-03 03:05:00 | `SAMPLE_TOR_SW_01` | <span style='color:red'>**CRC_ERROR**</span> | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| 2026-07-03 03:06:00 | `SAMPLE_TOR_SW_01` | <span style='color:red'>**LINK_DOWN**</span> | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |
| 2026-07-03 03:12:00 | `SAMPLE_TOR_SW_01` | <span style='color:red'>**TICKET_ESCALATED**</span> | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team. |
| 2026-07-03 03:30:00 | `SAMPLE_TOR_SW_01` | <span style='color:red'>**CRC_ERROR**</span> | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1 |

---
## 💡 [교육용] AWS DCO 직무 이해 가이드 팁
1. **Heartbeat (주기적 신호)**: DCO에서는 장비가 살아있는지 주기적으로 통신 상태를 체크합니다. 로그의 대부분이 INFO 등급의 Heartbeat인 이유입니다.
2. **Hardware Maintenance (SSD 교체, 팬 고장)**: 서버 드라이브 장애나 팬 속도 저하는 하드웨어 점검 작업으로 이어집니다. 위 로그에서 티켓 생성 후 하드웨어 부품을 핫스왑(핫 플러그) 교체하는 일련의 흐름을 보실 수 있습니다.
3. **Cabling & Link down (물리 케이블 이슈)**: CRC error 증가는 대개 광케이블(LC-LC multi-mode) 커넥터 오염이나 물리적 손상일 확률이 높습니다. 케이블을 교체하고 포트 링크가 다시 UP 상태로 회복되는 프로세스를 시각화한 것입니다.