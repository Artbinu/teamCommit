
# ✅ 보안 취약점 개선 사항

이 문서는 기존 급여 조회 프로그램의 보안 취약점을 어떻게 개선했는지 설명합니다.

---

## 1. ❌ SQL Injection 위험 → ✅ 파라미터 바인딩 사용
- **기존 문제**: 사용자 입력이 직접 SQL 쿼리에 삽입됨.
- **개선**:
  - 모든 SQL 쿼리에 대해 파라미터 바인딩 (`%s`) 사용.

```python
cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
```


