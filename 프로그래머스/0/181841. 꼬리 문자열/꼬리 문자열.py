def solution(str_list, ex):
    answer = ''
    for idx in range(len(str_list)):
        if ex not in str_list[idx]:
            answer += str_list[idx]
    return answer
