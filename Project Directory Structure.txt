payroll_project/
│
├── main.py                 # 메인 실행 파일 (콘솔 모드)
├── models.py               # 데이터 모델: 사용자, 급여
├── auth.py                 # 로그인 및 인증 관련 로직
├── payroll.py              # 급여 추가/조회/수정 등 비즈니스 로직
├── utils.py                # 해시, 보안 검사, 유효성 검사 함수
├── logger.py               # 로그 기록 기능
│
├── test/                   # 유닛 테스트 모듈
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_utils.py
│   └── test_payroll.py
│
├── data/                   # 추후 JSON 또는 SQLite 데이터 저장소
│   ├── users.json
│   ├── salaries.json
│   └── logs.txt
│
└── README.md               # 프로젝트 설명 및 사용법 문서
