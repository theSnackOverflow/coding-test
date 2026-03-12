import sys 
input = sys.stdin.readline

hours, mins = map(int, input().split())
time = int(input())

mins += time
hours = (hours + (mins // 60)) % 24
mins = mins % 60

print(hours, mins)