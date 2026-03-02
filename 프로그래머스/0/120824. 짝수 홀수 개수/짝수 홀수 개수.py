def solution(num_list):
    a, b = 0, 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            a += 1
        else: b += 1
    return [a, b]
