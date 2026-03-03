def solution(age):
    answer = ''
    dict = {"0":"a", "1":"b", "2":"c", "3":"d", "4":"e", "5":"f", "6":"g", "7":"h", "8":"i", "9":"j"}
    age = str(age)
    
    for idx in range(len(age)):
        answer += dict[age[idx]]
    return answer