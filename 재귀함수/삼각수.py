def triangle_number(n):
    # 베이스 케이스
    if n == 1:
        return 1

    # 재귀 케이스
    return triangle_number(n - 1) + n


# 테스트 코드
for i in range(1, 11):
    print(triangle_number(i))