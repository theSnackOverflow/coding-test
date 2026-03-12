import sys
input = sys.stdin.readline

n = int(input())

for idx in range(n):
    arr = list(input().split())
    result = 0
    for idx in range(len(arr)):
        if idx == 0:
            result = float(arr[idx])
        else:
            if arr[idx] == "@":
                result *= 3 
            if arr[idx] == "%":
                result += 5
            if arr[idx] == "#":
                result -= 7  
    print(f"{result:.2f}")