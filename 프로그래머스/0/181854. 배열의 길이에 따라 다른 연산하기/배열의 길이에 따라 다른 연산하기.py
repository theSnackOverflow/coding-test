def solution(arr, n):
    if len(arr) % 2 != 0:
        return [arr[idx] + n if idx % 2 == 0 else arr[idx] for idx in range(len(arr))]
    else: return [arr[idx] + n if idx % 2 == 1 else arr[idx] for idx in range(len(arr))]
