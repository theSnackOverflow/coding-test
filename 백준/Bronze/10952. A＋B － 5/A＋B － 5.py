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
    if a+b != 0:
        print(a+b)