n = int(input())
dp = [0 for _ in range(n+1)]
if n>=2:
    dp[2] = 3
for i in range(4,n+1):
    if i%2==1:
        dp[i]=0
    else:
        dp[i] = dp[i-2]*3 + 2*sum(dp[:i-2])+2

print(dp[n])