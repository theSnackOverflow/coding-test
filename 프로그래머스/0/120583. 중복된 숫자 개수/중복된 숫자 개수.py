def solution(array, n):
    count = 0
    for idx in range(len(array)):
        if n == array[idx]:
            count += 1
    return count
