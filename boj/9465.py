t=int(input())
for _ in range(t):
    n=int(input())
    nums=[]
    nums.append(list(map(int,input().split())))
    nums.append(list(map(int,input().split())))
    dp=[[0 for _ in range(n)] for _ in range(2)]
    dp[0][0]=nums[0][0]
    dp[1][0]=nums[1][0]
    if n>1:
        dp[0][1]=dp[1][0]+nums[0][1]
        dp[1][1]=dp[0][0]+nums[1][1]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2])+nums[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2])+nums[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))
