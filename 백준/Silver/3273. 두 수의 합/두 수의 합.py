import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()

answer = 0
left, right = 0, n-1

while left < right:
    s = nums[left] + nums[right]
    
    if s == target:
        answer += 1
        left += 1
        right -= 1
    elif s < target:
        left += 1
    else:
        right -= 1
    
print(answer)