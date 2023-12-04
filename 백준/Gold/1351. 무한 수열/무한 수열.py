import math
N,P,Q =map(int,input().split())
dp={}
def dfs(n):
    if n==0:
        return 1
    elif n in dp.keys():
        return dp[n]
    else:
        dp[n]=dfs(math.floor(n/P))+dfs(math.floor(n/Q))
        return dp[n]
print(dfs(N))