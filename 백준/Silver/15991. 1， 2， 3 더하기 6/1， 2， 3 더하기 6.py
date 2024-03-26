import sys
input = sys.stdin.readline
T = int(input().rstrip())
dp=[0 for _ in range(100001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
for i in range(4,100001):
    if(i>=6):
        dp[i] = dp[i-6]+dp[i-4]+dp[i-2]
    else:
        dp[i] = dp[i-4]+dp[i-2]

for _ in range(T):
    n = int(input().rstrip())
    print(dp[n]%1000000009)
