import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())
    
a, b = int(lines[0]), int(lines[2])

if lines[1] == "*": print(a * b)
elif lines[1] == "+": print(a + b)