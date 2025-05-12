
# ✅ 보안 취약점 개선 사항

이 문서는 기존 급여 조회 프로그램의 보안 취약점을 어떻게 개선했는지 설명합니다.

---

## 1. ❌ 평문 비밀번호 저장 → ✅ 해시(SHA-256) 저장
- **기존 문제**: 데이터베이스에 비밀번호가 평문으로 저장되어 있었음.
- **개선**:
  - `hashlib.sha256()`을 사용하여 비밀번호를 해싱.
  - 사용자 추가 시 MariaDB 내장 함수 `SHA2(비밀번호, 256)`을 사용하여 해시 저장.

```python
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

---

## 2. ❌ 로그인 실패 무제한 시도 → ✅ 로그인 실패 횟수 제한 및 잠금
- **기존 문제**: 로그인 실패 시도에 대한 제한이 없어 무차별 대입 공격(Brute-force)에 취약.
- **개선**:
  - 로그인 실패 5회 시 30분 잠금 (`LOCK_DURATION`)
  - 로그인 성공 시 실패 횟수 초기화

```python
if global_login_attempts >= 5:
    if current_time < lock_until:
        print(f"⛔ 로그인 실패 5회! {remaining_time}분 후 다시 시도하세요.")
```

---

## 3. ❌ 관리자 권한 확인 미흡 → ✅ 명확한 역할 구분
- **기존 문제**: 단순히 ID가 `"admin"`인지로만 관리자 여부 판단.
- **개선**:
  - 역할을 명확히 구분하여 `"admin"` 사용자만 관리자 기능 수행 가능.
  - 추가로 DB의 `role` 컬럼으로 사용자 권한 관리하는 것도 추천 (추후 확장 가능).

---

## 4. ❌ SQL Injection 위험 → ✅ 파라미터 바인딩 사용
- **기존 문제**: 사용자 입력이 직접 SQL 쿼리에 삽입됨.
- **개선**:
  - 모든 SQL 쿼리에 대해 파라미터 바인딩 (`%s`) 사용.

```python
cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
```


