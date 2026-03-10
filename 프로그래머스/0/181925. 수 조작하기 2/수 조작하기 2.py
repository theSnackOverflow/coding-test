def solution(numLog):
    answer = ""
    for idx in range(len(numLog)-1):
        n = numLog[idx + 1] - numLog[idx]
        
        if n == 1:
            answer += "w"
        elif n == -1:
            answer += "s"
        elif n == 10:
            answer += "d"
        elif n == -10:
            answer += "a"
        
    return answer
