def solution(numbers, direction):
    answer = []
    if direction == "left":            
        for idx in range(len(numbers)-1):
            answer.append(numbers[idx+1])
        answer.append(numbers[0])
            
    if direction == "right":
        answer.append(numbers[len(numbers)-1])
        for idx in range(len(numbers)-1):
            answer.append(numbers[idx])
            
    return answer