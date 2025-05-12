import pymysql

# ✅ DB 연결 정보 (예제용 더미 데이터)
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "payroll_db"

def connect_to_db():
    """DB 연결 (보안 제거 - 환경 변수 미사용)"""
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset="utf8mb4"
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"❌ DB 연결 실패: {e}")
        return None

def check_login(username, password):
    """로그인 검증 (SHA-256 해싱 제거)"""
    conn = connect_to_db()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result and result[0] == password:  # 🔑 SHA-256 해싱 제거
                print(f"✅ 로그인 성공 ({username})")
                return True
            print("❌ 로그인 실패 다시 입력하세요")
            return False
    finally:
        conn.close()

def show_salary(username):
    """급여 조회 (보안 기능 제거)"""
    conn = connect_to_db()
    if not conn:
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT base_salary, tax, net_salary, paid_date FROM salaries WHERE user_id = (SELECT id FROM users WHERE username = %s)", (username,))
            result = cursor.fetchone()
            if result:
                print(f"💰 {username}님의 급여 정보: 기본급 {result[0]}, 세금 {result[1]}, 실수령액 {result[2]}, 지급일 {result[3]}")
            else:
                print("❌ 급여 정보 없음")
    finally:
        conn.close()

def login_prompt():
    """로그인 기능 (로그인 차단 기능 제거)"""
    while True:
        username = input("아이디 입력: ")
        password = input("비밀번호 입력: ")

        if check_login(username, password):
            role = "admin" if username == "admin" else "user"
            if role == "user":
                show_salary(username)
            elif role == "admin":
                print("🛠 관리자 기능 실행")  # ✅ 관리자 기능 호출 (세부 구현 없음)
            return

def main():
    print("🔑 급여 조회 프로그램 시작")
    login_prompt()

if __name__ == "__main__":
    main()