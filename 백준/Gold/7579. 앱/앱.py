import sys
input = sys.stdin.readline
N, M = map(int,input().split())
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))
dp=[[0 for _ in range(sum(c)+1)] for _ in range(N+1)]
result = sum(c)

for i in range(1,N+1):
    byte = m[i]
    cost = c[i]

    for j in range(1,sum(c)+1):
        if j<cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)
if M!=0:
    print(result)
else:
    print(0)