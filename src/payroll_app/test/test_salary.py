import unittest
import os
import json
from salary import add_salary, edit_salary, delete_salary, view_salary

class TestSalaryFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 테스트 전 필요한 초기 설정 (예: 파일 삭제)
        if os.path.exists("data/salaries.json"):
            os.remove("data/salaries.json")

    def test_add_salary(self):
        # 급여 추가 테스트
        add_salary(1, 1000, 100, 900, "2025-05-11")
        
        with open("data/salaries.json", "r", encoding="utf-8") as f:
            salaries = json.load(f)
        
        self.assertEqual(len(salaries), 1)  # 급여 정보가 1개여야 한다.
        self.assertEqual(salaries[0]["user_id"], 1)
        self.assertEqual(salaries[0]["base_salary"], 1000)

    def test_edit_salary(self):
        # 급여 수정 테스트
        add_salary(1, 1000, 100, 900, "2025-05-11")
        edit_salary(1, 1200, 120, 1080, "2025-06-11")
        
        with open("data/salaries.json", "r", encoding="utf-8") as f:
            salaries = json.load(f)
        
        self.assertEqual(salaries[0]["base_salary"], 1200)  # 수정된 급여가 반영되어야 한다.
        self.assertEqual(salaries[0]["tax"], 120)

    def test_delete_salary(self):
        # 급여 삭제 테스트
        add_salary(1, 1000, 100, 900, "2025-05-11")
        delete_salary(1)
        
        with open("data/salaries.json", "r", encoding="utf-8") as f:
            salaries = json.load(f)
        
        self.assertEqual(len(salaries), 0)  # 급여 정보가 0개여야 한다.

    def test_view_salary(self):
        # 급여 조회 테스트
        add_salary(1, 1000, 100, 900, "2025-05-11")
        add_salary(2, 1500, 150, 1350, "2025-05-12")
        
        with open("data/salaries.json", "r", encoding="utf-8") as f:
            salaries = json.load(f)
        
        self.assertEqual(salaries[0]["user_id"], 1)  # 첫 번째 급여 정보 확인
        self.assertEqual(salaries[1]["user_id"], 2)  # 두 번째 급여 정보 확인

    @classmethod
    def tearDownClass(cls):
        # 테스트 후 정리 작업 (예: 생성된 파일 삭제)
        if os.path.exists("data/salaries.json"):
            os.remove("data/salaries.json")


if __name__ == "__main__":
    unittest.main()
