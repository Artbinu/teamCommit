import unittest
import sys
import time
sys.path.append("C:\\Git\\teamCommit\\src\\payroll_system")  # ✅ 절대 경로 추가

from payroll_system.main import check_login, show_salary, global_login_attempts, LOCK_DURATION  

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        """각 테스트 실행 전 전역 변수 초기화"""
        global global_login_attempts
        global_login_attempts = 0

    def test_correct_login(self):
        """올바른 아이디와 비밀번호로 로그인"""
        print("✅ test_correct_login 시도")
        self.assertTrue(check_login("admin", "admin123"))
        print("✅ test_correct_login 성공")

    def test_wrong_password(self):
        """아이디는 맞지만 비밀번호가 틀린 경우"""
        print("✅ test_wrong_password 시도")
        self.assertFalse(check_login("admin", "wrongpass"))
        print("✅ test_wrong_password 성공")

    def test_nonexistent_user(self):
        """존재하지 않는 사용자로 로그인 시도"""
        print("✅ test_nonexistent_user 시도")
        self.assertFalse(check_login("unknown", "password"))
        print("✅ test_nonexistent_user 성공")

    def test_failed_attempts_limit(self):
        """5회 연속 로그인 실패 후 계정 잠금"""
        print("✅ test_failed_attempts_limit 시도")
        for _ in range(5):
            check_login("admin", "wrongpass")

        # 30분 동안 로그인 차단 확인
        self.assertFalse(check_login("admin", "admin123"))  # 🔒 로그인 제한 확인
        print("✅ test_failed_attempts_limit 성공")

        # 30분 후 로그인 가능 여부 테스트
        time.sleep(LOCK_DURATION)  # 실제 테스트 환경에서는 직접 lock_until 값을 수정하는 것이 더 효율적
        self.assertTrue(check_login("admin", "admin123"))
        print("✅ test_failed_attempts_limit - 로그인 제한 해제 성공")

    def test_success_after_reset(self):
        """로그인 성공 후 실패 횟수 초기화"""
        print("✅ test_success_after_reset 시도")
        check_login("admin", "admin123")
        self.assertEqual(global_login_attempts, 0)  # ✅ 실패 횟수 초기화 확인
        print("✅ test_success_after_reset 성공")

    def test_show_salary(self):
        """급여 조회 기능 테스트"""
        print("✅ test_show_salary 시도")
        show_salary("user1")  # 실제 DB 데이터 필요
        print("✅ test_show_salary 성공")

if __name__ == "__main__":
    unittest.main()