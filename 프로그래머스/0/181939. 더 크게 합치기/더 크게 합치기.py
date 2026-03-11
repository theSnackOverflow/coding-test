def solution(a, b):
    answer = 0
    int1 = int(str(a) + str(b))
    int2 = int(str(b) + str(a))
    
    if int1 > int2 : 
        answer = int1
    else:
        answer = int2
    
    return answer
