n=int(input())
tmp = list(map(int,input().split()))
nums = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if tmp[i]>tmp[j]:
            nums[i] = max(nums[i], nums[j]+1)
print(max(nums))