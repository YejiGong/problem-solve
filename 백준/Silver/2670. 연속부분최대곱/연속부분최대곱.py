N = int(input())
nums = list(float(input()) for _ in range(N))
dp = [0 for _ in range(N)]
dp[0] = nums[0]
for i in range(1,N):
    dp[i] = max(nums[i], dp[i-1] * nums[i])

res = max(dp)
print("%.3f"%res)