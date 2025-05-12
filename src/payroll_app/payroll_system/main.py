import hashlib
import time

# 사용자 데이터 저장
users = {
    "admin": {"password_hash": hashlib.sha256(b"admin123").hexdigest(), "role": "admin", "login_attempts": 0, "lock_time": None},
    "user1": {"password_hash": hashlib.sha256(b"user123").hexdigest(), "role": "user", "login_attempts": 0, "lock_time": None}
}

salaries = {
    "user1": {"base_salary": 5000, "tax": 500, "net_salary": 4500, "paid_date": "2025-05-01"}
}

LOCK_DURATION = 30 * 60  # 30분

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    user = users.get(username)

    if user is None:
        print("❌ 사용자 없음")
        return False

    current_time = time.time()
    if user["lock_time"] and current_time < user["lock_time"]:
        print("⛔ 로그인 실패 5회. 30분 후 다시 시도하세요.")
        return False

    if user["password_hash"] == hash_password(password):
        print(f"✅ 로그인 성공 ({username})")
        user["login_attempts"] = 0  # 로그인 성공 시 실패 횟수 초기화
        user["lock_time"] = None
        return True
    else:
        user["login_attempts"] += 1
        print(f"❌ 로그인 실패 ({user['login_attempts']}회)")

        if user["login_attempts"] >= 5:
            user["lock_time"] = current_time + LOCK_DURATION
            print("⛔ 로그인 실패 5회! 30분 동안 잠금")

        return False

def login_prompt():
    while True:
        username = input("아이디 입력: ")
        password = input("비밀번호 입력: ")

        if check_login(username, password):
            role = users[username]["role"]
            if role == "user":
                show_salary(username)
            elif role == "admin":
                admin_actions()
            break  # 로그인 성공 시 루프 종료
        else:
            print("❗ 로그인 실패. 다시 입력하세요.")

def show_salary(username):
    if username in salaries:
        print(f"💰 {username}님의 급여 정보: {salaries[username]}")
    else:
        print("❌ 급여 정보 없음")

def admin_actions():
    print("🛠 관리자 기능:")
    print("1. 사용자 추가")
    print("2. 사용자 삭제")
    print("3. 급여 추가/수정")
    choice = input("선택: ")

    if choice == "1":
        new_user = input("새 사용자 아이디: ")
        new_password = input("새 비밀번호: ")
        users[new_user] = {"password_hash": hash_password(new_password), "role": "user", "login_attempts": 0, "lock_time": None}
        print(f"✅ 사용자 {new_user} 추가 완료")

    elif choice == "2":
        del_user = input("삭제할 사용자 아이디: ")
        if del_user in users:
            del users[del_user]
            print(f"✅ 사용자 {del_user} 삭제 완료")
        else:
            print("❌ 사용자 없음")

    elif choice == "3":
        target_user = input("급여 정보를 추가/수정할 사용자 아이디: ")
        if target_user in users:
            base_salary = int(input("기본 급여 입력: "))
            tax = int(input("세금 입력: "))
            net_salary = base_salary - tax
            salaries[target_user] = {"base_salary": base_salary, "tax": tax, "net_salary": net_salary, "paid_date": "2025-05-01"}
            print(f"✅ 급여 정보 수정 완료 ({target_user})")
        else:
            print("❌ 사용자 없음")

def main():
    print("🔑 급여 조회 프로그램 시작")
    login_prompt()

if __name__ == "__main__":
    main()