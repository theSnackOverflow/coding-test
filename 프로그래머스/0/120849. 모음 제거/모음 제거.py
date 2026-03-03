def solution(my_string):
    vowels = 'aeiou'
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in vowels:
            answer += my_string[i]
    return answer
