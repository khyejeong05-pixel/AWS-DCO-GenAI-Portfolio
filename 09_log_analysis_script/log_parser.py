# -*- coding: utf-8 -*-
"""
AWS DCO 인턴십 직무 이해를 위한 교육용 DCO 로그 분석 스크립트
외부 라이브러리 설치 없이 오직 파이썬 표준 라이브러리만 사용합니다.
"""

import os

def analyze_logs(log_file_path, output_file_path):
    # 1. 입력용 로그 파일이 실제로 존재하는지 체크합니다.
    if not os.path.exists(log_file_path):
        print(f"[오류] 입력 파일 '{log_file_path}'을 찾을 수 없습니다.")
        return

    print(f"[{log_file_path}] 파일 분석을 시작합니다...")

    # 데이터를 담을 파이썬 내장 자료형(변수) 초기화
    total_lines = 0               # 1. 전체 로그 줄 수
    severity_counts = {}          # 2. 심각도별 개수를 저장할 딕셔너리 (예: {'INFO': 10, 'WARNING': 2})
    event_counts = {}             # 3. 이벤트별 개수를 저장할 딕셔너리 (예: {'Normal heartbeat': 15})
    warning_or_critical_logs = [] # 4. WARNING 또는 CRITICAL 등급의 로그를 저장할 리스트
    key_incidents = []            # 5. CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 관련 주요 이벤트 요약

    # 2. 로그 파일을 'r'(읽기) 모드로 한 줄씩 읽습니다.
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip() # 줄 바꿈 문자(\n) 및 앞뒤 공백 제거
            if not line:        # 빈 줄은 처리하지 않고 건너뜁니다
                continue
            
            total_lines += 1

            # 로그 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            # ' | ' 구분자를 기준으로 데이터를 분할(split)합니다.
            parts = [p.strip() for p in line.split('|')]
            
            # 정상적인 로그 형식이 아니면 건너뜁니다.
            if len(parts) < 5:
                continue
            
            timestamp = parts[0]
            device = parts[1]
            severity = parts[2]
            event = parts[3]
            message = parts[4]

            # --- 분석 2: 심각도(INFO/WARNING/ERROR) 개수 카운트 ---
            # 딕셔너리에 기존 값이 없으면 0으로 시작하여 1을 더해나가갑니다.
            severity_counts[severity] = severity_counts.get(severity, 0) + 1

            # --- 분석 3: 이벤트명별 개수 카운트 ---
            event_counts[event] = event_counts.get(event, 0) + 1

            # --- 분석 4: 경고 등급 이상의 중요한 로그 모으기 ---
            if severity in ["WARNING", "CRITICAL", "ERROR"]:
                warning_or_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

            # --- 분석 5: 주요 이벤트 필터링 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) ---
            # 로그 내용(event, message)에 핵심 키워드가 포함되어 있는지 검사합니다.
            event_lower = event.lower()
            message_lower = message.lower()

            is_crc = ("crc" in event_lower) or ("crc" in message_lower)
            is_link_down = ("link down" in event_lower) or ("link_down" in event_lower) or ("link down" in message_lower)
            is_ticket_escalated = ("escalated" in event_lower) or ("escalated" in message_lower)

            if is_crc or is_link_down or is_ticket_escalated:
                category = []
                if is_crc: category.append("CRC_ERROR")
                if is_link_down: category.append("LINK_DOWN")
                if is_ticket_escalated: category.append("TICKET_ESCALATED")
                
                key_incidents.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "category": ", ".join(category),
                    "event": event,
                    "message": message
                })

    # 3. 분석 결과를 바탕으로 마크다운(Markdown) 보고서 내용을 리스트로 작성합니다.
    markdown_content = []
    markdown_content.append("# 📊 AWS DCO 교육용 샘플 로그 분석 결과 보고서")
    markdown_content.append(f"**생성 시간**: 2026-07-19\n")
    markdown_content.append("---")
    
    # [1] 전체 로그 요약
    markdown_content.append("## 1. 📈 전체 로그 요약")
    markdown_content.append(f"- **전체 로그 라인 수**: {total_lines}개\n")
    
    # [2] 심각도별 분포 테이블 생성
    markdown_content.append("## 2. 🛡️ 심각도별 분포")
    markdown_content.append("| 심각도 (Severity) | 개수 (Count) | 비율 (Percentage) |")
    markdown_content.append("| --- | --- | --- |")
    for sev, count in sorted(severity_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_lines) * 100
        markdown_content.append(f"| `{sev}` | {count}개 | {percentage:.1f}% |")
    markdown_content.append("")

    # [3] 이벤트 발생 빈도 순위 테이블 생성
    markdown_content.append("## 3. 🏷️ 주요 이벤트 발생 빈도 Top 10")
    markdown_content.append("| 순위 | 이벤트명 (Event) | 발생 개수 | 비율 |")
    markdown_content.append("| --- | --- | --- | --- |")
    sorted_events = sorted(event_counts.items(), key=lambda x: x[1], reverse=True)
    for idx, (evt, count) in enumerate(sorted_events[:10], 1):
        percentage = (count / total_lines) * 100
        markdown_content.append(f"| {idx} | {evt} | {count}개 | {percentage:.1f}% |")
    markdown_content.append("")

    # [4] 경고 로그 표 출력
    markdown_content.append("## 4. ⚠️ 주의 및 경고 로그 목록 (WARNING / ERROR / CRITICAL)")
    if warning_or_critical_logs:
        markdown_content.append("| 시간 | 장비명 (Device) | 심각도 | 이벤트 | 상세 내용 |")
        markdown_content.append("| --- | --- | --- | --- | --- |")
        for log in warning_or_critical_logs:
            markdown_content.append(f"| {log['timestamp']} | `{log['device']}` | **{log['severity']}** | {log['event']} | {log['message']} |")
    else:
        markdown_content.append("- 감지된 경고 등급의 로그가 없습니다.")
    markdown_content.append("")

    # [5] 주요 핵심 이벤트 요약 표 출력
    markdown_content.append("## 5. 🔍 핵심 장애 및 운영 관리 요약 (CRC_ERROR, LINK_DOWN, TICKET_ESCALATED)")
    markdown_content.append("데이터 센터 네트워크 인프라 및 티켓 관리에서 추적이 필요한 핵심 이벤트 항목입니다.")
    if key_incidents:
        markdown_content.append("| 시간 | 장비명 (Device) | 감지 분류 (Category) | 이벤트 | 상세 내용 |")
        markdown_content.append("| --- | --- | --- | --- | --- |")
        for incident in key_incidents:
            markdown_content.append(f"| {incident['timestamp']} | `{incident['device']}` | <span style='color:red'>**{incident['category']}**</span> | {incident['event']} | {incident['message']} |")
    else:
        markdown_content.append("- 필터링 조건에 부합하는 주요 이벤트를 찾지 못했습니다.")
    markdown_content.append("")

    # [6] 인턴십 직무 교육용 인사이트 가이드 추가
    markdown_content.append("---")
    markdown_content.append("## 💡 [교육용] AWS DCO 직무 이해 가이드 팁")
    markdown_content.append("1. **Heartbeat (주기적 신호)**: DCO에서는 장비가 살아있는지 주기적으로 통신 상태를 체크합니다. 로그의 대부분이 INFO 등급의 Heartbeat인 이유입니다.")
    markdown_content.append("2. **Hardware Maintenance (SSD 교체, 팬 고장)**: 서버 드라이브 장애나 팬 속도 저하는 하드웨어 점검 작업으로 이어집니다. 위 로그에서 티켓 생성 후 하드웨어 부품을 핫스왑(핫 플러그) 교체하는 일련의 흐름을 보실 수 있습니다.")
    markdown_content.append("3. **Cabling & Link down (물리 케이블 이슈)**: CRC error 증가는 대개 광케이블(LC-LC multi-mode) 커넥터 오염이나 물리적 손상일 확률이 높습니다. 케이블을 교체하고 포트 링크가 다시 UP 상태로 회복되는 프로세스를 시각화한 것입니다.")

    # 4. 분석 결과 마크다운 파일을 지정한 경로에 쓰기(write) 합니다.
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(markdown_content))

    print(f"[분석 완료] 결과가 '{output_file_path}' 파일에 저장되었습니다.")

# 메인 실행 지점
if __name__ == "__main__":
    # 스크립트 파일이 위치한 디렉토리 파악
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 후보 경로 리스트 순서대로 검증 (CWD -> 스크립트 디렉토리 -> 컨테이너 루트)
    possible_log_paths = [
        "sample_dco_log.txt",
        os.path.join(script_dir, "sample_dco_log.txt"),
        "/sample_dco_log.txt"
    ]
    
    # 존재하는 첫 번째 파일을 선택
    LOG_FILE = None
    for path in possible_log_paths:
        if os.path.exists(path):
            LOG_FILE = path
            break
            
    # 만약 파일이 하나도 없다면, 스크립트 디렉토리 내부 경로를 기본값으로 지정
    if not LOG_FILE:
        LOG_FILE = os.path.join(script_dir, "sample_dco_log.txt")
        
    # 결과 파일도 입력 파일이 있는 위치(또는 스크립트 폴더)에 맞춰 생성하도록 자동 설정
    if LOG_FILE and os.path.exists(LOG_FILE):
        log_dir = os.path.dirname(os.path.abspath(LOG_FILE))
        OUTPUT_FILE = os.path.join(log_dir, "incident_summary.md")
    else:
        OUTPUT_FILE = os.path.join(script_dir, "incident_summary.md")
        
    analyze_logs(LOG_FILE, OUTPUT_FILE)
