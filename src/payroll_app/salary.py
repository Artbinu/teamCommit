import os
import json

SALARY_FILE = "data/salaries.json"

# 급여 정보 추가
def add_salary(user_id, base_salary, tax, net_salary, paid_date):
    if not os.path.exists("data"):
        os.makedirs("data")  # data 폴더가 없으면 생성

    if not os.path.exists(SALARY_FILE):
        with open(SALARY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)  # 빈 리스트로 파일 생성

    with open(SALARY_FILE, "r+", encoding="utf-8") as f:
        salaries = json.load(f)
        
        new_salary = {
            "user_id": user_id,
            "base_salary": base_salary,
            "tax": tax,
            "net_salary": net_salary,
            "paid_date": paid_date
        }
        salaries.append(new_salary)
        
        f.seek(0)  # 파일의 처음으로 이동
        json.dump(salaries, f, ensure_ascii=False, indent=4)
    print(f"✅ {user_id}의 급여 정보가 추가되었습니다.")

# 급여 정보 수정
def edit_salary(user_id, new_base_salary, new_tax, new_net_salary, new_paid_date):
    if not os.path.exists(SALARY_FILE):
        print("❌ 급여 파일이 존재하지 않습니다.")
        return

    with open(SALARY_FILE, "r+", encoding="utf-8") as f:
        salaries = json.load(f)
        found = False
        for salary in salaries:
            if salary["user_id"] == user_id:
                salary["base_salary"] = new_base_salary
                salary["tax"] = new_tax
                salary["net_salary"] = new_net_salary
                salary["paid_date"] = new_paid_date
                found = True
                break
        
        if not found:
            print("❌ 해당 사용자 급여 정보가 존재하지 않습니다.")
            return
        
        f.seek(0)  # 파일의 처음으로 이동
        json.dump(salaries, f, ensure_ascii=False, indent=4)
    print(f"✅ {user_id}의 급여 정보가 수정되었습니다.")

# 급여 정보 삭제
def delete_salary(user_id):
    if not os.path.exists(SALARY_FILE):
        print("❌ 급여 파일이 존재하지 않습니다.")
        return

    with open(SALARY_FILE, "r+", encoding="utf-8") as f:
        salaries = json.load(f)
        salaries = [salary for salary in salaries if salary["user_id"] != user_id]
        
        f.seek(0)  # 파일의 처음으로 이동
        json.dump(salaries, f, ensure_ascii=False, indent=4)
    print(f"✅ {user_id}의 급여 정보가 삭제되었습니다.")

# 급여 정보 조회
def view_salary(user_id):
    if not os.path.exists(SALARY_FILE):
        print("❌ 급여 파일이 존재하지 않습니다.")
        return

    with open(SALARY_FILE, "r", encoding="utf-8") as f:
        salaries = json.load(f)
        for salary in salaries:
            if salary["user_id"] == user_id:
                print(f"급여 정보: {salary}")
                return
        
    print("❌ 해당 사용자 급여 정보가 존재하지 않습니다.")
