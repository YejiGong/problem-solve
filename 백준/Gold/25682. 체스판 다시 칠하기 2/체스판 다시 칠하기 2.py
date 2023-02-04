import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
boards=[list(input().strip()) for _ in range(N)]

def check(color):
    dp=[[0]*(M+1) for i in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2==0:
                value = boards[i][j]!=color
            else:
                value = boards[i][j]==color
            dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]-dp[i][j]+value
    count=int(1e9)
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            count = min(count, dp[i+K-1][j+K-1]-dp[i+K-1][j-1]-dp[i-1][j+K-1]+dp[i-1][j-1])
    return count


print(min(check('W'), check('B')))