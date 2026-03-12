import sys 
input = sys.stdin.readline

hours, mins = map(int, input().split())
time = int(input())

share = 0
mins = mins + time

if mins >= 60:
    share = (mins // 60)
    hours += share
    mins = (mins % 60)
    hours = (hours % 24)

print(hours, mins)