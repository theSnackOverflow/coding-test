def solution(num_list):
    even, odd = "", ""
    for idx in range(len(num_list)):
        if num_list[idx] % 2 == 0:
            even += str(num_list[idx])
        else:
            odd += str(num_list[idx])
            
    return int(even) + int(odd)
