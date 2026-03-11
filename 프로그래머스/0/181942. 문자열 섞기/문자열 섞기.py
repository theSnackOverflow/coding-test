def solution(str1, str2):
    n = len(str1)
    answer = ""
    for i in range(n):
        answer += str1[i]
        answer += str2[i]

    return answer
