def solution(num_list, n):
    answer = []
    for idx in range(n, len(num_list)):
        answer.append(num_list[idx])
    for idx in range(0, n):
        answer.append(num_list[idx])
    return answer
