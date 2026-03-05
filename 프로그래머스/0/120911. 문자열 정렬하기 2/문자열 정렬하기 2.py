def solution(my_string):
    my_string = list(my_string.lower())
    answer, temp = '', []
    n = len(my_string)
    for i in range(n):
        for j in range(i+1, n):
            if my_string[i] > my_string[j]:
                temp = my_string[i]
                my_string[i] = my_string[j]
                my_string[j] = temp
        answer += my_string[i]
    return answer    
        
