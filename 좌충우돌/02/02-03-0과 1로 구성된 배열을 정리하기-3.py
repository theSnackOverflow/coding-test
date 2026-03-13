# 문제 설명
# 0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

# 입력: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 출력: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# 입력: [1, 1], 출력: [1, 1]

# 풀이 3. 투 포인터 (교재 풀이)
def solution (arr):
  left, right = 0, len(arr)-1

  while left < right:
    while left < len(arr) and arr[left] == 0:
      left += 1
    while right >=0 and arr[right] == 1:
      right -= 1
    if left < right:
      arr[left], arr[right] = 0, 1
      left, right = left+1, right-1

  return arr

input_1 = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0] 
input_2 = [1, 1]


print(solution(input_1)) # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print(solution(input_2)) # [1, 1]

