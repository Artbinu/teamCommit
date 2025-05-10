# main.py

from auth import login
from user_management import register_user, edit_user, delete_user, list_users
from salary import add_salary, edit_salary, delete_salary, view_salary
from logger import show_logs


def user_menu(username):
    while True:
        print(f"\n👤 사용자 메뉴 ({username})")
        print("1. 내 급여 조회")
        print("0. 로그아웃")
        choice = input("선택: ").strip()
        if choice == "1":
            view_salary(username)
        elif choice == "0":
            print("👋 로그아웃합니다.\n")
            break
        else:
            print("❌ 잘못된 입력입니다.")

def admin_menu(username):
    while True:
        print(f"\n🔧 관리자 메뉴 ({username})")
        print("1. 사용자 목록 보기")
        print("2. 사용자 등록")
        print("3. 사용자 수정")
        print("4. 사용자 삭제")
        print("5. 급여 정보 추가")
        print("6. 급여 정보 수정")
        print("7. 급여 정보 삭제")
        print("8. 감사 로그 보기")
        print("0. 로그아웃")
        choice = input("선택: ").strip()
        if choice == "1":
            list_users()
        elif choice == "2":
            register_user()
        elif choice == "3":
            edit_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            add_salary()
        elif choice == "6":
            edit_salary()
        elif choice == "7":
            delete_salary()
        elif choice == "8":
            show_logs()
        elif choice == "0":
            print("👋 로그아웃합니다.\n")
            break
        else:
            print("❌ 잘못된 입력입니다.")

def main():
    print("💼 급여 조회 프로그램 시작")
    while True:
        username, role = login()
        if role == "user":
            user_menu(username)
        elif role == "admin":
            admin_menu(username)

if __name__ == "__main__":
    main()
