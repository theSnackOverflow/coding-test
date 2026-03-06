def solution(num_str):
    answer = 0
    num_str = [int(num) for num in num_str]
    for num in num_str:
        answer += num
    return answer
