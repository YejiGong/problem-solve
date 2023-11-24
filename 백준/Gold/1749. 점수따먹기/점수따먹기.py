import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = [[0]*(M+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
maxResult = -1e9
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+nums[i][j]

for i in range(1,N+1):
    for j in range(1,M+1):
        for p in range(i,N+1):
            for q in range(j,M+1):
                #(p,q) ~ (i,j)
                maxResult = max(maxResult, dp[p][q]-dp[i-1][q]-dp[p][j-1]+dp[i-1][j-1])

print(maxResult)

