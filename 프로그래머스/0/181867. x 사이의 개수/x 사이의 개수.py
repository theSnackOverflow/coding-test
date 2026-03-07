def solution(myString):
    answer = []
    strArr = myString.split("x")
    for str in strArr:
        answer.append(len(str))
    return answer
