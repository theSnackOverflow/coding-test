import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))
answer = ''

for num in nums:
    if num < x:
        answer += (str(num) + " ")
print(answer.strip())
       

