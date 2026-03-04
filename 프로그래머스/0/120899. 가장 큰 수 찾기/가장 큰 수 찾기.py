def solution(array):
    idx = 0
    max = array[0]
    for num in range(len(array)):    
        if array[num] > max:
            max = array[num]
            idx = num
    return [max, idx]
