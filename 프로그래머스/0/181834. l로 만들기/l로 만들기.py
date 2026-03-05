def solution(myString):
    answer = ''
    for char in myString:
        if char < 'l':
            answer += 'l'
        else:
            answer += char
    return answer
