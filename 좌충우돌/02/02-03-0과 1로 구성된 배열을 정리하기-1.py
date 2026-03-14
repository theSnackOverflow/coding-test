# 문제 설명
# 0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

# 입력: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 출력: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# 입력: [1, 1], 출력: [1, 1]

# 풀이 1. count() 메서드 이용하기 - 1 (나의 풀이)
def solution (arr):
  answer = []
  count_one, count_zero = arr.count(1), arr.count(0)

  for _ in range(count_zero):
    answer.append(0)
  for _ in range(count_one):
    answer.append(1)
    
  return answer

input_1 = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0] 
input_2 = [1, 1]


print(solution(input_1)) # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print(solution(input_2)) # [1, 1]

