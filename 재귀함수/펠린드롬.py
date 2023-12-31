def is_palindrome(my_str):
    if len(my_str) <= 1:
        return True
    # 내가 쓴 코드
    #elif my_str[0] == my_str[-1]:
     #   if is_palindrome(my_str[1:-1]) is True:
     #       return True
     #   else:
     #       return False
    #else:
     #   return False
    if my_str[0] != my_str[-1]:
        return False

    return is_palindrome(my_str[1:-1])

# 굳이 True, False로 결과값 지정해주지 않아도 하위문제의 결과를 불러오기 때문에 최종 결과가 True, False의 형태로 나옴

# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))
