def solution(arr, delete_list):
    answer = []
    for idx in range(len(arr)):
        if arr[idx] not in delete_list:
            answer.append(arr[idx])
    return answer
