def solution(arr1, arr2):
    num_arr1, num_arr2 = 0, 0
    
    if len(arr1) > len(arr2): return 1
    elif len(arr1) < len(arr2): return -1
    else: 
        n = len(arr1)
        for item in arr1: num_arr1 += int(item)
        for item in arr2: num_arr2 += int(item)
        
        if num_arr1 == num_arr2: return 0
        elif num_arr1 < num_arr2: return -1
        else: return 1
