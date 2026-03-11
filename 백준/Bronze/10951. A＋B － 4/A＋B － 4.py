import sys
input = sys.stdin.readline

lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line.strip())
    
for line in lines:
    a, b = map(int, line.split())
    print(a+b)