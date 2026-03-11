import sys
input = sys.stdin.readline

n = int(input())
for idx in range(n):
    a, b = map(int, input().split())
    print(f"Case #{idx+1}: {a+b}")