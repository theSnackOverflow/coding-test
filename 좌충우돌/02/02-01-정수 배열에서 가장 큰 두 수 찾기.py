# 문제 설명
# 정수로 이루어진 배열이 주어질 때, 
# 가장 큰 두 수를 찾아 [가장 큰 값, 둘째로 큰 값]을 반환하는 함수를 완성하라.

# 입력: [3, -1, 5, 0, 7, 4, 9, 1], 출력: [9, 7]
# 입력: [7], 출력: [7]

def solution (arr) :
  if len(arr) == 1:
    return [arr[0]]
  else:
    max_1, max_2 = 0, 0
    for item in arr:
      if max_1 < item:
        max_2 = max_1
        max_1 = item

  return [max_1, max_2]

print(solution([3, -1, 5, 7, 4, 9, 1]))
print(solution([7]))