import sys
input = sys.stdin.readline

# 입력1 : 시 분 초
# 입력2 : 요리시간
h, m, s = map(int, input().split())
c = int(input())

s += c
m += s // 60
s %= 60

h += m // 60
m %= 60
h %= 24


# 출력 : 시 분 초
print(h, m , s)