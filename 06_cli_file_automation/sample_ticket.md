# [교육용 샘플 데이터 / FOR EDUCATIONAL USE ONLY]
본 문서는 교육용으로 생성된 샘플 데이터이며, 실제 AWS 인프라, 장비, 티켓 시스템 또는 고객 정보와 아무런 관련이 없습니다.

## 교육용 샘플 티켓 (EDU-SAMPLE-TICKET-001)

- **티켓 ID**: EDU-SAMPLE-TICKET-001
- **발생 시간**: 2026-07-07 15:00:00 KST (EDU-TIME-SAMPLE)
- **샘플 장비명**: SAMPLE_TOR_SW_01 (EDU-SAMPLE-DEVICE)
- **이벤트**: CRC error 증가 후 Link Down 발생 (CRC Error Increase & Link Down Event)
- **심각도**: Severity 2 (EDU-SAMPLE-SEV-2)
- **관찰 내용**: 
  - SAMPLE_TOR_SW_01 장비의 특정 포트(EDU-PORT-SAMPLE-01)에서 인터페이스 CRC 에러 수치가 급격히 증가함.
  - 에러 누적 이후 해당 인터페이스의 링크 상태가 Down으로 변경되는 이벤트가 추가적으로 관찰됨.
- **Escalation 필요 여부**: 필요함 (Escalation to EDU-SAMPLE-L2-SUPPORT)
- **보안 주의사항**:
  - 본 티켓 및 관찰 로그에는 실제 IP 주소, 장비 시리얼 넘버, 계정 정보, 고객 개인 식별 정보를 절대 포함하지 마십시오.
  - 외부 네트워크로의 접속이나 비인가된 명령 테스트를 수행하지 마십시오.
