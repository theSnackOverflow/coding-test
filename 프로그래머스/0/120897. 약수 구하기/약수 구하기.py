def solution(n):
    answer = [1]
    for num in range(2, n+1):
        if n % num == 0:
            answer.append(num)
    return answer
