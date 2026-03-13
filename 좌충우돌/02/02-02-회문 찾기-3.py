# 문제 설명
# 주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환하라.

# 풀이 3. 투 포인터 이용하기
def solution (str):
  left, right = 0, len(str)-1

  while left < right:
    if str[left] != str[right]:
      return False
    left += 1
    right -= 1
    
  return True

input_1 = "madam" 
input_2 = "tomato"
input_3 = "racecar"
input_4 = "rotor"
input_5 = "별똥별"
input_6 = "코끼리"

print(solution(input_1)) # True
print(solution(input_2)) # False
print(solution(input_3)) # True
print(solution(input_4)) # True
print(solution(input_5)) # True
print(solution(input_6)) # False
