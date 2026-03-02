def solution(num_list):
    sorted_num_list = [0 for num in range(len(num_list))]
    for idx in range(len(num_list) ):
        
        sorted_num_list[idx] = num_list[len(num_list) -1 - idx]
        
    return sorted_num_list
