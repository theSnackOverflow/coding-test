def solution(num_list):
    odd_sum, even_sum = 0, 0
    for idx in range(len(num_list)):
        if idx % 2 == 0:
            odd_sum += num_list[idx]
        else: 
            even_sum += num_list[idx]  
    if odd_sum >= even_sum : return odd_sum
    else: return even_sum 
    
