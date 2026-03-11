import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().strip()
    print(s[0] + s[-1])