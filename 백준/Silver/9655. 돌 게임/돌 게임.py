N=int(input())
dp = [N for _ in range(N+1)]
for i in range(1,N+1):
    dp[i] = max(dp[i-1]-1, dp[i-1]-3)
    if dp[i]<=0:
        print('CY' if i%2==0 else 'SK')
        break