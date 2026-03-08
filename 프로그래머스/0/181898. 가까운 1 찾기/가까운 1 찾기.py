def solution(arr, idx):
    for num in range(idx, len(arr)):
        if arr[num] == 1:
            return num
    else: return -1
