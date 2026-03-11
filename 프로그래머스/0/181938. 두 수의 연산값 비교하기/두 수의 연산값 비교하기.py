def solution(a, b):
    answer = 0
    num = int(str(a) + str(b))
    
    if num >= 2*a*b:
        answer = num
    else:
        answer = 2*a*b
    
    return answer
