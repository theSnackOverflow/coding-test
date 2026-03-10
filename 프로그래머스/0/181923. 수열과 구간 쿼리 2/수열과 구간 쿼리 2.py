def solution(arr, queries):
    answer = []
    for query in queries:
        temp = []
        for num in range(query[0], query[1] + 1):
            
            if arr[num] > query[2]:
                temp.append(arr[num])

                
        if temp:
            answer.append(min(temp))
        else:
            answer.append(-1)

    return answer
