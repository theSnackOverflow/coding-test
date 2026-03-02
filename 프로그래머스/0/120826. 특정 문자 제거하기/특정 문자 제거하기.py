def solution(my_string, letter):
    answer = ''
    for num in range(len(my_string)):
        if letter != my_string[num]:
            answer += my_string[num]
    return answer
