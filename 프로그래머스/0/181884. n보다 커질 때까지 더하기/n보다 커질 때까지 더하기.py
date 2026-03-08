def solution(numbers, n):
    sum = 0
    for idx in range(len(numbers)):
        sum += numbers[idx]
        if sum > n:
            break
    return sum
