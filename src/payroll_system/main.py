import hashlib
import time
import db_connection

LOCK_DURATION = 30 * 60  # 30분 (초 단위)
#LOCK_DURATION = 15  #테스트용

global_login_attempts = 0  # 전체 로그인 실패 횟수
lock_until = 0  # 로그인 잠금 해제 시간

def hash_password(password):
    """비밀번호를 SHA-256으로 해시화"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    """MariaDB 10에서 사용자 인증"""
    global global_login_attempts, lock_until
    conn = db_connection.connect_to_db()

    if not conn:
        print("❌ DB 연결 실패")
        return False

    current_time = time.time()
    
    # ⛔ 로그인 잠금 여부 확인
    if global_login_attempts >= 5:
        if current_time < lock_until:
            remaining_time = int((lock_until - current_time) / 60)
            print(f"⛔ 로그인 실패 5회! {remaining_time}분 후 다시 시도하세요.")
            return False
        else:
            global_login_attempts = 0  # 30분 후 실패 횟수 초기화

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()

            # ✅ 올바른 로그인 처리
            if result and result[0] == hash_password(password):
                print(f"✅ 로그인 성공 ({username})")
                global_login_attempts = 0  # 로그인 성공 시 실패 횟수 초기화
                return True

            # ❌ 로그인 실패 처리
            global_login_attempts += 1
            remaining_attempts = 5 - global_login_attempts
            print(f"❌ 로그인 실패 ({global_login_attempts}회째 시도, 남은 시도: {remaining_attempts}회)")

            if global_login_attempts >= 5:
                lock_until = current_time + LOCK_DURATION
                print("⛔ 로그인 실패 5회! 30분 동안 로그인 차단")

            return False
    except Exception as e:
        print(f"❌ 로그인 확인 실패: {e}")
        return False
    finally:
        conn.close()

def show_salary(username):
    """MariaDB 10에서 사용자의 급여 정보 조회"""
    conn = db_connection.connect_to_db()
    
    if not conn:
        print("❌ DB 연결 실패")
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT base_salary, tax, net_salary, paid_date FROM salaries WHERE user_id = (SELECT id FROM users WHERE username = %s)", (username,))
            result = cursor.fetchone()

            if result:
                print(f"💰 {username}님의 급여 정보: 기본급 {result[0]}, 세금 {result[1]}, 실수령액 {result[2]}, 지급일 {result[3]}")
            else:
                print("❌ 급여 정보 없음")
    except Exception as e:
        print(f"❌ 급여 정보 조회 실패: {e}")
    finally:
        conn.close()

def admin_actions():
    """MariaDB 10에서 관리자 기능 수행"""
    conn = db_connection.connect_to_db()
    
    if not conn:
        print("❌ DB 연결 실패")
        return

    try:
        while True:  # 종료를 선택할 때까지 반복
            print("===🛠 관리자 기능 🛠===")
            print("1. 사용자 추가")
            print("2. 사용자 삭제")
            print("3. 급여 추가/수정")
            print("4. 사용자 목록 조회")
            print("5. 종료")

            choice = input("선택: ")
            
            if choice == "5":
                print("🔚 관리자 모드 종료")
                break  # 반복문 탈출
            
            with conn.cursor() as cursor:  # cursor 사용
                if choice == "1":
                    new_user = input("새 사용자 아이디: ")
                    new_password = input("새 비밀번호: ")
                    full_name = input("사용자 이름: ")
                    cursor.execute("INSERT INTO users (username, password_hash, full_name, role) VALUES (%s, SHA2(%s, 256), %s, 'user')", (new_user, new_password, full_name))
                    conn.commit()
                    print(f"✅ 사용자 {new_user}({full_name}) 추가 완료")

                elif choice == "2":
                    del_user = input("삭제할 사용자 아이디: ")
                    cursor.execute("DELETE FROM users WHERE username = %s", (del_user,))
                    conn.commit()
                    print(f"✅ 사용자 {del_user} 삭제 완료")

                elif choice == "3":
                    target_user = input("급여 정보를 추가/수정할 사용자 아이디: ")
                    base_salary = int(input("기본 급여 입력: "))
                    tax = int(input("세금 입력: "))
                    net_salary = base_salary - tax
                    cursor.execute("INSERT INTO salaries (user_id, base_salary, tax, net_salary, paid_date) VALUES ((SELECT id FROM users WHERE username = %s), %s, %s, %s, CURDATE())", (target_user, base_salary, tax, net_salary))
                    conn.commit()
                    print(f"✅ 급여 정보 수정 완료 ({target_user})")

                elif choice == "4":
                    cursor.execute("SELECT username, full_name FROM users")
                    users = cursor.fetchall()
                    print("📜 사용자 목록:")
                    for user in users:
                        print(f"👤 {user[0]} ({user[1]})")  # 사용자 아이디와 이름 출력
    except Exception as e:
        print(f"❌ 관리자 기능 수행 실패: {e}")
    finally:
        conn.close()  # 반복문이 끝날 때 한 번만 연결 닫기

def login_prompt():
    """사용자 로그인 프로세스"""
    global global_login_attempts
    while global_login_attempts < 5:
        username = input("아이디 입력: ")
        password = input("비밀번호 입력: ")

        if check_login(username, password):
            role = "admin" if username == "admin" else "user"
            if role == "user":
                show_salary(username)
            elif role == "admin":
                admin_actions()
            return  # 로그인 성공 시 종료
    print("🚫 너무 많은 로그인 실패! 프로그램 종료")

def main():
    print("🔑 급여 조회 프로그램 시작")
    login_prompt()

if __name__ == "__main__":
    main()