def solution(a, d, included):
    answer = 0
    arr = []
    for n in range(0, len(included)):
        arr.append(a + n * d)
    
    for idx in range(len(arr)):
        answer += arr[idx] * int(included[idx])
    
    return answer
