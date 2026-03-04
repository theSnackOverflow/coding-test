def solution(numbers):
    temp = []
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            temp.append(numbers[i] * numbers[j])
    temp.sort(reverse=True)
    return temp[0]
    
