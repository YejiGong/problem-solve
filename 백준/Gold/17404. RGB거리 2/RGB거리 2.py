N= int(input())
price = [list(map(int,input().split())) for _ in range(N)]
ans = 1e9
candidate = [(0,1,2),(0,2,1),(1,2,0),(1,0,2),(2,1,0),(2,0,1)]
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for i in range(N)]
    dp[0][i] = price[0][i]
    for j in range(1,N):
        dp[j][0] = price[j][0]+min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = price[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = price[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i!=j:
            ans = min(ans, dp[-1][j])
print(ans)