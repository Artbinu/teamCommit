import unittest
import os
from user_management import register_user, edit_user, delete_user, list_users
from auth import save_users, load_users

class TestUserManagementFunctions(unittest.TestCase):

    def setUp(self):
        self.test_user = {"username": "admin", "password_hash": "adminhash", "role": "admin"}
        save_users([self.test_user])  # 초기 사용자 저장

    def test_register_user(self):
        # 사용자 등록 테스트
        register_user("test_user", "test_password", "user")
        users = load_users()
        self.assertEqual(len(users), 2)  # 새로 등록된 사용자 포함
        self.assertEqual(users[-1]["username"], "test_user")

    def test_edit_user(self):
        # 사용자 수정 테스트
        edit_user("admin", "new_password")
        users = load_users()
        self.assertEqual(users[0]["password_hash"], "new_password")  # 비밀번호 수정 확인

    def test_delete_user(self):
        # 사용자 삭제 테스트
        delete_user("admin")
        users = load_users()
        self.assertEqual(len(users), 0)  # 삭제된 후 사용자가 없어야 함

    def test_list_users(self):
        # 사용자 목록 확인
        users = list_users()
        self.assertGreater(len(users), 0)  # 사용자 목록이 비지 않도록

    def tearDown(self):
        # 테스트 후 users 파일 삭제
        if os.path.exists("data/users.json"):
            os.remove("data/users.json")

if __name__ == "__main__":
    unittest.main()
