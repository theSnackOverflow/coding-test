import sys

n = input()
for num in sorted({int(num) for num in sys.stdin}):
    print(num)