# 문제 설명
# 주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환하라.

# 입력: madam, 출력: True
# 입력: tomato, 출력: False

# 풀이 1. 반복문
# def solution (str):
#   reverse_str = '' 
#   for idx in range(len(str)):
#     reverse_str += str[-(idx + 1)]

#   return str == reverse_str

# 풀이 2. 인덱스 슬라이싱
def solution (str):
  return str == str[::-1]

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

# 0 1 2 3 4  
# -1 -2 -3 -4 -5