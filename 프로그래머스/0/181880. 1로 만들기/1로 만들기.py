answer = 0
def isOne(num):
    global answer
    if num == 1: return num
    else:
        if num % 2 == 0:
                num = num // 2
                answer += 1
                isOne(num)
        else: 
            num = (num - 1) // 2
            answer += 1
            isOne(num)
        
        
def solution(num_list):
    global answer
    for num in num_list:
        isOne(num)
    return answer