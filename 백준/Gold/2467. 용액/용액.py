import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
diff = 1e15
ans = []

for i in range(N):
    idx = bisect_left(nums, -nums[i])
    for j in range(-1,2): #idx의 앞 뒤 (-1,0,1)
        if 0<=j+idx<N and i!=j+idx: #0 제외하고 앞 뒤 
            tmp = nums[j+idx]
            if abs(nums[i]+tmp) <= diff:
                diff = abs(nums[i]+tmp)
                ans = [nums[i], tmp]
print(*sorted(ans))
