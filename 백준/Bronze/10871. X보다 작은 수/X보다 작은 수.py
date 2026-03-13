import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

print(" ".join([str(num) for num in nums if num < x]))
       

