import sys
input = sys.stdin.readline

n = int(input())
num_arr = list(map(int, input().split()))
v = int(input())

count = 0
for num in num_arr:
    if num == v:
        count += 1

print(count)