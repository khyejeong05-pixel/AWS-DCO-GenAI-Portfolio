# Shift Handover

> **교육용 샘플 데이터 (Educational Sample Data)**  
> 본 문서는 교육용 샘플 데이터를 기반으로 작성되었습니다. 실제 AWS 시스템, 장비, 티켓 또는 운영 절차를 의미하지 않습니다.

## 1. 가장 먼저 확인할 Ticket

**EDU-TKT-2026-0202**

- 우선순위: 1
- 현재 상태: Open (Escalated)
- 판단 근거: 관련 샘플 서버가 6대로 연속적이고 전원 상태가 복귀되지 않았기 때문.

## 2. 우선순위별 Ticket 상태와 판단 근거

|우선순위|Ticket|상태|판단 근거|
|---|---|---|---|
|1|EDU-TKT-2026-0202|Open (Escalated)|관련 샘플 서버가 6대로 연속적이고 전원 상태가 복귀되지 않았기 때문|
|2|EDU-TKT-2026-0201|Open|Link Down 이후 반복 상태 변화가 기록됨|
|3|EDU-TKT-2026-0203|Monitoring|SSD 상태 확인 및 유지보수 일정 미기록|
|4|EDU-TKT-2026-0204|Resolved|Fan RPM 정상 회복|

## 3. Open 상태 Ticket

### EDU-TKT-2026-0202
- 입력 전압 경고 지속
- 장애 기록 없음
- 정상 Dual-feed 상태 미복구

### EDU-TKT-2026-0201
- Link Down 이후 Link 복구
- 추가 Link 상태 변화 기록
- 서비스 이용 가능하나 반복 상태 변화는 설명되지 않음

## 4. Monitoring 상태 Ticket

### EDU-TKT-2026-0203
- SSD Predictive Failure
- 서비스 이용 가능
- 유지보수 일정 및 교체 시점 미기록

## 5. Resolved 상태 Ticket

### EDU-TKT-2026-0204
- Fan RPM 정상 범위로 회복
- Ticket 상태: Resolved

## 6. 아직 확인되지 않은 정보

- EDU-TKT-2026-0202: 정상 Dual-feed 상태 복구 여부
- EDU-TKT-2026-0201: 반복 상태 변화에 대한 설명
- EDU-TKT-2026-0203: 유지보수 일정 및 SSD 교체 시점
- EDU-TKT-2026-0204: Fan RPM 저하 원인

## 7. 다음 담당자가 확인할 사항

- EDU-TKT-2026-0202의 전원 상태 및 Dual-feed 복구 여부 확인
- EDU-TKT-2026-0201의 Link 상태 변화 지속 여부 확인
- EDU-TKT-2026-0203의 유지보수 일정 확인
- EDU-TKT-2026-0204의 추가 기록 확인

## 8. 3줄 인수인계 요약 
- 최우선 확인 대상은 EDU-TKT-2026-0202로, 입력 전압 경고가 지속되고 정상 Dual-feed 상태가 아직 복구되지 않은 Open 티켓입니다.
- EDU-TKT-2026-0201은 Open, EDU-TKT-2026-0203은 Monitoring, EDU-TKT-2026-0204는 Resolved 상태이며, Link 상태 변화와 SSD 유지보수 일정 등 일부 정보는 아직 확인되지 않았습니다.
- 다음 담당자는 우선순위에 따라 Open 티켓의 현재 상태와 미확인 정보를 확인하고, Monitoring 티켓의 유지보수 일정 및 Resolved 티켓의 추가 기록 여부를 검토하면 됩니다.