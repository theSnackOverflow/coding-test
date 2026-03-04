def solution(s1, s2):
    result = 0
    if len(s1) <= len(s2):
        for num in range(len(s1)):
            if s1[num] in s2:
                result += 1
    else:
        for num in range(len(s2)):
            if s2[num] in s1:
                result += 1
    return result
