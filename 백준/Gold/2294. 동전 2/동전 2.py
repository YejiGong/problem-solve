n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [1e9 for _ in range(k+1)]
dp[0] = 0

for i in range(n):
    for j in range(1,k+1):
        if(coins[i]<=j):
            dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])

