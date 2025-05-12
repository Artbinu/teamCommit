import unittest
import sys
sys.path.append(r"C:\Git\teamCommit\src")  # ✅ 절대 경로 추가

from payroll_system.db_connection import connect_to_db  # ✅ 절대 경로 기반 import

class TestDBConnection(unittest.TestCase):

    def test_db_connection(self):
        """MariaDB 연결 테스트"""
        print("=========================================================")
        print("✅ DB 연결 테스트 시작")
        conn = connect_to_db()
        self.assertIsNotNone(conn)  # ✅ DB 연결 여부 확인
        if conn:
            print("✅ DB 연결 테스트 성공")
            print("=========================================================")
            conn.close()

if __name__ == "__main__":
    unittest.main()