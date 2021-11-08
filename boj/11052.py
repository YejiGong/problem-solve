import sys
n=int(sys.stdin.readline())
money=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0 for i in range(n+1)]
dp[1]=money[1]
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i], dp[i-j]+money[j])
print(dp[n])
