# 문제 설명
# 정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)

# 입력: arr = [1, 2, 3, 7, 5], s = 12, 출력: [2, 4]
# 인덱스 2부터 4까지의 합: 2 + 3 + 7 = 12
# 입력: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s = 15, 출력: [1, 5]

# 풀이 2. 투 포인터
def solution (arr, s):
  left = 0
  sub_total = 0
  for right in range(len(arr)):
    sub_total += arr[right]
    while left < right and sub_total > s:
      sub_total -= arr[left]
      left += 1
    if sub_total == s:
      return [left+1, right+1]
    
  return [-1]

arr_1 = [1, 2, 3, 7, 5]
s_1 = 12 # [2, 4]
arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_2 = 15 # [1, 5]
arr_3 = [1, 2, 3, 4]
s_3 = 0


print(solution(arr_1, s_1)) # 
print(solution(arr_2, s_2)) # 
print(solution(arr_3, s_3)) # [-1]

