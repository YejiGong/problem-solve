import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
l = 0
res = 0
num_set = {}

for r in range(0, N):
    if(nums[r] in num_set.keys()):
        num_set[nums[r]]+=1
    else:
        num_set[nums[r]] = 1
    while l<r and len(num_set.keys())>2:
        num_set[nums[l]] -= 1
        if num_set[nums[l]] == 0:
            num_set.pop(nums[l])
        l+=1
    res = max(res, r-l+1)


print(res)