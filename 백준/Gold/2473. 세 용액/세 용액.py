import sys
from bisect import bisect_left
input = sys.stdin.readline
N= int(input())
nums=list(map(int,input().split()))
nums.sort()
diff = float('inf')
ans= [0,0,0]
for i in range(N-2):
    if i>0 and nums[i] == nums[i-1]:
        continue
    left, right = i+1, N-1

    while left<right:
        sum = nums[i]+nums[left]+nums[right]
        if abs(sum)<abs(diff):
            ans=[nums[i], nums[left], nums[right]]
            diff=sum

        if sum<0:
            left+=1
        elif sum>0:
            right -=1
        else:
            print(nums[i], nums[left], nums[right])
            sys.exit(0)

print(*sorted(ans))