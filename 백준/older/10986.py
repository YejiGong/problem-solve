import sys
input=sys.stdin.readline
n, m = map(int,input().split())
nums=list(map(int,input().split()))
dp=[0 for _ in range(m)]
dp[0]=1
tmp=0
for i in range(n):
    tmp+=nums[i]
    dp[tmp%m]+=1

ans=0
for i in dp:
    ans+= i*(i-1)//2 #nC2
print(ans)
