import sys

nums = [int(num) for num in sys.stdin]

for idx in range(1, 31):
    if idx not in nums:
        print(idx)
    