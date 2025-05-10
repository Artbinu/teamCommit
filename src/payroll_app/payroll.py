# payroll.py

import json
import os
from datetime import datetime
from auth import load_users
from logger import log_action

SALARIES_FILE = "data/salaries.json"


# 급여 데이터 불러오기
def load_salaries():
    if not os.path.exists(SALARIES_FILE):
        return []
    with open(SALARIES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 급여 데이터 저장
def save_salaries(salaries):
    with open(SALARIES_FILE, "w", encoding="utf-8") as f:
        json.dump(salaries, f, indent=4, ensure_ascii=False)

# 사용자 급여 조회 (일반 사용자용)
def view_salary(username):
    salaries = load_salaries()
    print(f"\n💰 [{username}] 급여 내역:")
    found = False
    for s in salaries:
        if s["username"] == username:
            print(f"- 지급일: {s['paid_date']} | 기본급: {s['base_salary']} | 세금: {s['tax']} | 실수령액: {s['net_salary']}")
            found = True
    if not found:
        print("급여 정보가 없습니다.")

# 급여 추가 (관리자 전용)
def add_salary():
    username = input("급여를 추가할 사용자 아이디: ").strip()
    if not get_user(username):
        print("❌ 존재하지 않는 사용자입니다.")
        return

    base_salary = int(input("기본급: "))
    tax = int(input("세금: "))
    net_salary = base_salary - tax
    paid_date = input("지급일 (예: 2024-05-01): ").strip()

    salaries = load_salaries()
    new_entry = {
        "id": len(salaries) + 1,
        "username": username,
        "base_salary": base_salary,
        "tax": tax,
        "net_salary": net_salary,
        "paid_date": paid_date
    }
    salaries.append(new_entry)
    save_salaries(salaries)
    log_action("admin", f"급여 추가 - {username}")
    print("✅ 급여 정보가 추가되었습니다.")

# 급여 수정
def edit_salary():
    salaries = load_salaries()
    list_all_salaries(salaries)

    try:
        sid = int(input("수정할 급여 ID를 입력하세요: "))
    except ValueError:
        print("❌ 숫자를 입력하세요.")
        return

    for s in salaries:
        if s["id"] == sid:
            print(f"현재 정보: {s}")
            s["base_salary"] = int(input("새 기본급: "))
            s["tax"] = int(input("새 세금: "))
            s["net_salary"] = s["base_salary"] - s["tax"]
            s["paid_date"] = input("새 지급일 (YYYY-MM-DD): ")
            save_salaries(salaries)
            log_action("admin", f"급여 수정 - ID {sid}")
            print("✅ 수정 완료")
            return

    print("❌ 해당 ID의 급여 정보가 없습니다.")

# 급여 삭제
def delete_salary():
    salaries = load_salaries()
    list_all_salaries(salaries)

    try:
        sid = int(input("삭제할 급여 ID를 입력하세요: "))
    except ValueError:
        print("❌ 숫자를 입력하세요.")
        return

    updated_salaries = [s for s in salaries if s["id"] != sid]
    if len(updated_salaries) == len(salaries):
        print("❌ 해당 ID의 급여 정보가 없습니다.")
        return

    save_salaries(updated_salaries)
    log_action("admin", f"급여 삭제 - ID {sid}")
    print("✅ 삭제 완료")

# 전체 급여 출력 (관리자용)
def list_all_salaries(salaries):
    print("\n💼 전체 급여 목록:")
    for s in salaries:
        print(f"ID: {s['id']} | 사용자: {s['username']} | 지급일: {s['paid_date']} | 실수령: {s['net_salary']}")

# 사용자 존재 확인
def get_user(username):
    users = load_users()
    return any(u["username"] == username for u in users)
