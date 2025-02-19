N = int(input())
M = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
if(N>1):
    dp[2] = 2
for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

res = 1
prev = 0
for i in range(M):
    tmp = int(input())
    res *= dp[tmp - prev - 1]
    prev = tmp

res *= dp[N-prev]
print(res)