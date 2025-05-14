import pymysql

# ✅ MariaDB 10 연결 설정
DB_HOST = "artnas.tplinkdns.com"  # NAS의 IP 주소
DB_PORT = 3306  # MariaDB 기본 포트
DB_USER = "payadmin"  # DB 사용자 계정
DB_PASSWORD = "Ktezzang0919@"  # 비밀번호
DB_NAME = "payroll_db"  # 사용할 데이터베이스 이름

def connect_to_db():
    """MariaDB 10에 연결하는 함수"""
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