def solution(arr, k):
    if k % 2 == 1: return [item * k for item in arr]
    else: return [item + k for item in arr]