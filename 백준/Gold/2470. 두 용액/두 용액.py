N = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = abs(nums[0] + nums[-1])
queue = [nums[0], nums[-1]]
left = 0
right = N-1

while left<right:
    sum = nums[left]+nums[right]
    if abs(sum)<ans:
        ans = abs(sum)
        queue = [nums[left], nums[right]]
        if ans == 0:
            break
    if sum<0:
        left+=1
    else:
        right-=1

print(queue[0], queue[1])