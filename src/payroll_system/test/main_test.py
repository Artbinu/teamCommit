import unittest
import sys
sys.path.append(r"C:\Git\teamCommit\src\payroll_system\test")  # ✅ 절대 경로 추가

from test_db import TestDBConnection  # ✅ test 디렉터리 경로 수정
from test_main import TestMainFunctions

# ✅ 통합 테스트 실행
def run_tests():
    """모든 테스트를 실행하는 함수"""
    test_cases = [
        unittest.TestLoader().loadTestsFromTestCase(TestDBConnection),
        unittest.TestLoader().loadTestsFromTestCase(TestMainFunctions)
    ]

    all_tests = unittest.TestSuite(test_cases)
    runner = unittest.TextTestRunner()  # ✅ 인스턴스 생성
    runner.run(all_tests)  # ✅ 테스트 실행

if __name__ == "__main__":
    run_tests()