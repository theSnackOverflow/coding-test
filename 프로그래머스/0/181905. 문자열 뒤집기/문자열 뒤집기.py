def solution(my_string, s, e):
    answer = ''
    list = [my_string[:s], my_string[s:e+1], my_string[e+1:]]
    answer = list[0] + list[1][::-1] + list[2]
    return answer