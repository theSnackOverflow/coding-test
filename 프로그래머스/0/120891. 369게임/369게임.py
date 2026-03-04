def solution(order):
    answer = 0
    order = str(order)
    for idx in range(len(order)):
        if order[idx] in "369":
            answer += 1
    return answer
