def solution(arr, intervals):
    answer = []
    for itv in intervals:
        for idx in range(itv[0], itv[1]+1):
            answer.append(arr[idx])
    return answer
