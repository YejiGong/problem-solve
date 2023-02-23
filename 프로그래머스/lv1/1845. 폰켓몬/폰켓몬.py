def solution(nums):
    N=len(nums)
    queue=[]
    for i in range(N):
        if nums[i] not in queue:
            queue.append(nums[i])
    if len(queue)>N/2:
        return N/2
    else:
        return len(queue)