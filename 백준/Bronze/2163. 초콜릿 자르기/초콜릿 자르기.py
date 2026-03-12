import sys
input = sys.stdin.readline

num_rows, num_cols = map(int, input().split())

count = (num_rows - 1) + num_rows * (num_cols - 1)

print(count)