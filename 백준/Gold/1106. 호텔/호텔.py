C, N = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dp=[float('INF') for _ in range(C+100)]
dp[0] =0
for fee,num in graph:
    for i in range(num, C+100):
        dp[i] = min(dp[i-num]+fee, dp[i])

print(min(dp[C:]))