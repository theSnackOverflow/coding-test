def solution(my_string, m, c):
    answer = ''
    arr = []
    num_rows = int(len(my_string) / m)
    for i in range(num_rows):
        arr.append(my_string[i * m: m * (1 + i)])
    
    for item in arr:
        answer += item[c-1]
    
    return answer