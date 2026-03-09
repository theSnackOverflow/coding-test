def solution(intStrs, k, s, l):
    answer = []
    for item in intStrs:
        integer = int(item[s:s+l])
        if integer > k : answer.append(integer)
    return answer