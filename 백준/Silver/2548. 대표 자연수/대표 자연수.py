N=int(input())
nums = list(map(int,input().split()))
nums.sort()
sum_res = sum(nums)
candidate_num = 1e9
candidate = 1e9
for i in range(N):
    res = sum(nums[i:]) - nums[i]*(N-i) + nums[i]*i - sum(nums[:i])
    if res < candidate_num:
        candidate_num = res
        candidate = nums[i]
    elif res == candidate_num:
        candidate = min(candidate, nums[i])
print(candidate)







