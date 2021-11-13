import sys
n=int(sys.stdin.readline())
money=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[money[0]]+[[0,0,0] for _ in range(n-1)]

for i in range(n):
    for j in range(3):
        dp[i][j]=min([dp[i-1][k]+money[i][j] for k in range(3) if k!=j])
        
print(min(dp[n-1]))
