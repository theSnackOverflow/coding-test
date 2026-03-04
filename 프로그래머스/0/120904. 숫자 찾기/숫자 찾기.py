def solution(num, k):
    nums = list(str(num))
    
    for idx in range(len(nums)):
        if nums[idx] == str(k):
            return idx + 1
    return -1
