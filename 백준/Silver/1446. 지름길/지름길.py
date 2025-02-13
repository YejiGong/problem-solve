N,D = map(int,input().split())
dp = [i for i in range(D+1)]
arr = [list(map(int,input().split())) for i in range(N)]
arr.sort()
for r,e,d in arr:
    for i in range(1,D+1):
        if e == i:
            dp[i] = min(dp[i], dp[r]+d)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)
print(dp[-1])