def solution(my_string, n):
    answer = ''
    for num in range(len(my_string)):
        for _ in range(n):
            answer += my_string[num]
    return answer
