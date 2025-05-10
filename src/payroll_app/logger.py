# logger.py

import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "audit.log")

# 로그 디렉토리가 없으면 생성
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 작업 로그 기록 함수
def log_action(user, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] 사용자: {user} | 작업: {action}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

# 로그 보기 (옵션)
def show_logs():
    if not os.path.exists(LOG_FILE):
        print("❌ 로그 파일이 없습니다.")
        return

    print("\n📜 감사 로그:")
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())
