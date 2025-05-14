import pymysql

# ✅ MariaDB 10 연결 설정


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