import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    R, S = input().split()
    R = int(R)
    
    for char in S:
        print(char * R, end="")
    print()
    
    