def fib_optimized(n):
    previous = 0
    current = 1
    for i in range(1, n):
        # temp = current   <- 내가 쓴 코드
        # current = previous + current
        # previous = temp
        # 아래처럼 한 줄로 줄일 수 있음
        current, previous = current + previous, current
    return current

# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
