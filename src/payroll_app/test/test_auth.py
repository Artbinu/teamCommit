import unittest
import os
from auth import hash_password, load_users, save_users, login

class TestAuthFunctions(unittest.TestCase):

    def setUp(self):
        self.test_user = {"username": "admin", "password_hash": hash_password("admin123"), "role": "admin"}
        save_users([self.test_user])  # 초기 사용자 저장

    def test_hash_password(self):
        # 비밀번호 해시화 테스트
        password = "admin123"
        hashed_password = hash_password(password)
        self.assertEqual(hashed_password, self.test_user["password_hash"])

    def test_login_success(self):
        # 로그인 성공 테스트
        user = login()  # 로그인 함수가 성공적으로 user를 반환한다고 가정
        self.assertIsNotNone(user)

    def test_login_fail(self):
        # 로그인 실패 테스트
        with self.assertRaises(Exception):  # 로그인 실패 시 예외 발생 가정
            login()

    def tearDown(self):
        # 테스트 후 users 파일 삭제
        if os.path.exists("data/users.json"):
            os.remove("data/users.json")

if __name__ == "__main__":
    unittest.main()
