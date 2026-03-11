import sys
input = sys.stdin.readline

s = input().strip()
eng = "abcdefghijklmnopqrstuvwxyz"

for c in eng:
    if c in s:
        print(s.index(c), end=" ")
    else: print(-1, end=" ")
