import sys
input = sys.stdin.readline

list = list(map(int, input().split()))
list.sort()

print(list[1])