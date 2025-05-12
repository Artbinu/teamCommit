import unittest
import main  # ✅ main.py의 기능을 가져와 테스트

class TestPayrollSystem(unittest.TestCase):

    def setUp(self):
        """각 테스트 전에 실패 횟수를 초기화"""
        main.global_login_attempts = 0

    def test_correct_login(self):
        """올바른 아이디와 비밀번호로 로그인"""
        self.assertTrue(main.check_login("admin", "admin123"))
        print("✅ test_correct_login 성공")

    def test_wrong_password(self):
        """아이디는 맞지만 비밀번호가 틀린 경우"""
        self.assertFalse(main.check_login("admin", "wrongpass"))
        print("✅ test_wrong_password 성공")

    def test_nonexistent_user(self):
        """존재하지 않는 사용자로 로그인 시도"""
        self.assertFalse(main.check_login("unknown", "password"))
        print("✅ test_nonexistent_user 성공")

    def test_failed_attempts_limit(self):
        """5회 연속 로그인 실패 후 계정 잠금"""
        for _ in range(5):
            main.check_login("admin", "wrongpass")  # 5회 실패
        self.assertFalse(main.check_login("admin", "admin123"))  # 🔒 계정이 잠겨야 성공
        print("✅ test_failed_attempts_limit 성공")

    def test_success_after_reset(self):
        """로그인 성공 후 실패 횟수 초기화"""
        main.check_login("admin", "admin123")  # 올바른 로그인
        self.assertEqual(main.global_login_attempts, 0)  # ✅ 실패 횟수 정상적으로 초기화 확인
        print("✅ test_success_after_reset 성공")

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestPayrollSystem))
    if result.wasSuccessful():
        print("✅ 모든 테스트 성공: 문제없음")