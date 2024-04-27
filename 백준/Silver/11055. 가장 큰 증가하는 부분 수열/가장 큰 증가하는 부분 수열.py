N=int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = arr[0]
for i in range(1,N):
    dp[i] = arr[i]
    for j in range(0, i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))