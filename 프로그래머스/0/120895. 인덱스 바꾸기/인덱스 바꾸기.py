def solution(my_string, num1, num2):
    answer = ''
    for idx in range(len(my_string)):
        if idx == num1:
            answer += my_string[num2]
        elif idx == num2:
            answer += my_string[num1]
        else:
            answer += my_string[idx]
    return answer
