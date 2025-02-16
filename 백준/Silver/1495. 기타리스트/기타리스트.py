N,S,M = map(int,input().split())
volume = list(map(int,input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            num1 = j + volume[i]
            num2 = j - volume[i]
            if 0 <= num1 <= M:
                dp[i+1][num1] = 1
            if 0 <= num2 <= M:
                dp[i+1][num2] = 1
ans = -1
for i in range(M+1):
    if dp[N][i] == 1:
        ans = i
print(ans)