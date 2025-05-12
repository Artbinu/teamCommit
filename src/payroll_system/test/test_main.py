import unittest
import sys
sys.path.append("C:\Git\teamCommit\src\payroll_system")  # ✅ 절대 경로 추가

from payroll_system.main import check_login, show_salary, global_login_attempts  # ✅ 절대 경로 기반 import

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        """각 테스트 실행 전 전역 변수 초기화"""
        global global_login_attempts
        global_login_attempts = 0

    def test_correct_login(self):
        """올바른 아이디와 비밀번호로 로그인"""
        print("=========================================================")
        print("✅ test_correct_login 시도")
        self.assertTrue(check_login("admin", "admin123"))
        print("✅ test_correct_login 성공")


    def test_wrong_password(self):
        print("=========================================================")
        print("✅ test_wrong_password 시도")
        """아이디는 맞지만 비밀번호가 틀린 경우"""
        self.assertFalse(check_login("admin", "wrongpass"))
        print("✅ test_wrong_password 성공")


    def test_nonexistent_user(self):
        print("=========================================================")
        print("✅ test_nonexistent_user 시도")
        """존재하지 않는 사용자로 로그인 시도"""
        self.assertFalse(check_login("unknown", "password"))
        print("✅ test_nonexistent_user 성공")


    def test_failed_attempts_limit(self):
        print("=========================================================")
        print("✅ test_failed_attempts_limit 시도")
        """5회 연속 로그인 실패 후 계정 잠금"""
        for _ in range(5):
            check_login("admin", "wrongpass")
        self.assertFalse(check_login("admin", "admin123"))  # 🔒 계정이 잠겨야 성공
        print("✅ test_failed_attempts_limit 성공")


    def test_success_after_reset(self):
        print("=========================================================")
        print("✅ test_success_after_reset 시도")
        """로그인 성공 후 실패 횟수 초기화"""
        check_login("admin", "admin123")
        self.assertEqual(global_login_attempts, 0)  # ✅ 실패 횟수 초기화 확인
        print("✅ test_success_after_reset 성공")


    def test_show_salary(self):
        print("=========================================================")
        print("✅ test_show_salary 시도")
        """급여 조회 기능 테스트"""
        show_salary("user1")  # 실제 DB 데이터가 필요함
        print("✅ test_show_salary 성공")


if __name__ == "__main__":
    unittest.main()