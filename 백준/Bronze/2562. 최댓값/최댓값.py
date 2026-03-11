import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))

max_val = max(nums)
print(max_val)
print(nums.index(max_val) + 1)