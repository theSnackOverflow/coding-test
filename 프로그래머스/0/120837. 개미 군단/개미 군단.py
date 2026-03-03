def solution(hp):
    answer, share, remain = 0, 0, 0
    share, remain = hp // 5, hp % 5
    answer += share
    share, remain = remain // 3, remain % 3
    answer += share + remain
    
    return answer
