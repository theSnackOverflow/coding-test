# 문제 설명
# 정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)

# 입력: arr = [1, 2, 3, 7, 5], s = 12, 출력: [2, 4]
# 인덱스 2부터 4까지의 합: 2 + 3 + 7 = 12
# 입력: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s = 15, 출력: [1, 5]

# 풀이 1. 이중 반복문으로 풀기
def solution (arr, s):
  for i in range(len(arr)):
    sub_total = 0
    for j in range(i, len(arr)):
      sub_total += arr[j]
      if sub_total == s:
        return [i+1, j+1]
    

  return [-1]

arr_1 = [1, 2, 3, 7, 5]
s_1 = 12 # [2, 4]
arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_2 = 15 # [1, 5]


print(solution(arr_1, s_1)) # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print(solution(arr_2, s_2)) # [1, 1]

