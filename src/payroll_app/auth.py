# auth.py

import json
import hashlib
import os

USERS_FILE = "data/users.json"


# 비밀번호 해시
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 사용자 목록 로드
def load_users():
    if not os.path.exists(USERS_FILE):
        return []  # 파일 없으면 빈 리스트
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# 사용자 정보 저장
def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

# 사용자 이름으로 사용자 찾기
def get_user_by_username(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return user
    return None

# 사용자 인증
def login():
    print("🔐 로그인")
    username = input("아이디: ").strip()
    password = input("비밀번호: ").strip()

    if not username or not password:
        print("❌ 아이디와 비밀번호를 모두 입력해야 합니다.")
        return None, None

    password_hash = hash_password(password)
    users = load_users()

    for user in users:
        if user["username"] == username and user["password_hash"] == password_hash:
            print(f"✅ 로그인 성공: {username} ({user['role']})")
            return username, user["role"]

    print("❌ 로그인 실패: 아이디 또는 비밀번호가 올바르지 않습니다.")
    return None, None
