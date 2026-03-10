def solution(num_list):
    num1, num2 = 1, 0
    for num in num_list:
        num1 *= num
        num2 += num
    num2 = num2**2
    
    if num1 < num2:
        return 1
    else:
        return 0
