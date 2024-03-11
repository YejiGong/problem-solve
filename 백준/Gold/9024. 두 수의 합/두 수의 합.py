import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    closet, closetCount = 1e9, 0
    for i in range(len(nums)):
        left, right = i+1, len(nums)-1
        while left<=right:
            mid = left+ (right-left)//2
            sum_ = nums[i] + nums[mid]
            if abs(k - sum_) < closet:
                closet = abs(k - sum_)
                closetCount = 1
            elif abs(k - sum_) == closet:
                closetCount +=1
            if sum_>k:
                right = mid - 1
            else:
                left = mid + 1
    print(closetCount)

