def power(x, n):
    if n == 0:
        return 1
    if n <= 1:
        return x
#내가 작성한 코드
#    if n % 2 == 1:
#        return power(x, n//2)*power(x, n//2)*x
#    else:
#        return power(x, n//2)*power(x, n//2)

    temp = power(x, n//2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

print(power(2, 3))
print(power(5, 0))
print(power(17, 5))
print(power(3, 17))
print(power(4, 18))