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

# is_palindrome(my_str[1: -1])를 리턴하는 이유:
# 첫 번째 문자와 마지막 문자가 동일한 경우 (else문), my_str[1: -1]가 팰린드롬이라면 my_str도 팰린드롬. 예를 들어, 'racecar'는 'r'로 시작하고 끝나기 때문에 'aceca'가 팰린드롬이라면 'racecar'도 팰린드롬.
# 하지만 my_str[1: -1]가 팰린드롬이 아니라면 my_str도 팰린드롬이 아님. 예를 들어 'roar'의 경우 'r'로 시작하고 끝나지만 'oa'가 팰린드롬이 아니기 때문에 'roar'도 팰린드롬이 아님.

# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))
