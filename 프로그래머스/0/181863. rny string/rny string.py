def solution(rny_string):
    answer = ''
    for idx in range(len(rny_string)): 
        if rny_string[idx] == "m":
            answer += "rn"
        else: answer += rny_string[idx]
    return answer
