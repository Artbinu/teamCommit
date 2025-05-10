# user_management.py

from auth import load_users, save_users, get_user_by_username, hash_password


# 사용자 등록
def register_user(username, password, role):
    users = load_users()
    
    if get_user_by_username(username):
        print("❌ 해당 아이디는 이미 존재합니다.")
        return
    
    password_hash = hash_password(password)
    new_user = {
        "username": username,
        "password_hash": password_hash,
        "role": role
    }
    users.append(new_user)
    save_users(users)
    print(f"✅ 사용자 '{username}'가 등록되었습니다.")

# 사용자 수정
def edit_user(username, new_username=None, new_password=None, new_role=None):
    users = load_users()
    user = get_user_by_username(username)
    
    if not user:
        print("❌ 사용자 찾을 수 없습니다.")
        return
    
    if new_username:
        user["username"] = new_username
    if new_password:
        user["password_hash"] = hash_password(new_password)
    if new_role:
        user["role"] = new_role
    
    save_users(users)
    print(f"✅ 사용자 '{username}'의 정보가 수정되었습니다.")

# 사용자 삭제
def delete_user(username):
    users = load_users()
    user = get_user_by_username(username)
    
    if not user:
        print("❌ 사용자 찾을 수 없습니다.")
        return
    
    users.remove(user)
    save_users(users)
    print(f"✅ 사용자 '{username}'가 삭제되었습니다.")

# 사용자 목록 조회
def list_users():
    users = load_users()
    if not users:
        print("❌ 등록된 사용자가 없습니다.")
        return
    
    print("📋 사용자 목록:")
    for user in users:
        print(f"아이디: {user['username']}, 역할: {user['role']}")
