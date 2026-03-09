def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query[0], query[1], query[2] 
        for i in range(s, e + 1):
            if i % k == 0 or k == 1:
                arr[i] += 1
            else:
                pass
        answer = arr
    return answer
