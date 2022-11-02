import sys
input=sys.stdin.readline
n, s = map(int,input().split())
nums = list(map(int,input().split()))
dp=[0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i]=dp[i-1]+nums[i-1]

ans = 100001
start=0
end=1
while start!=n:
    if dp[end] - dp[start]>=s:
        if end-start<ans:
            ans = end-start
        start+=1
    else:
        if end!=n:
            end+=1
        else:
            start+=1

if ans!=100001:
    print(ans)
else:
    print(0)
