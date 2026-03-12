import sys
input = sys.stdin.readline

for idx in range(int(input())):
    line = input().split()
    result = float(line[0])
    
    for op in line[1:]:
        if op == "@":
            result *= 3 
        if op == "%":
            result += 5
        if op == "#":
            result -= 7  
    print(f"{result:.2f}")