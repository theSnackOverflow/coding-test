def solution(myString):
    answer = [str for str in myString.split("x") if str != ""]
    answer.sort()
    return answer
