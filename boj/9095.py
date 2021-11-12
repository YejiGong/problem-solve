import sys
n=int(sys.stdin.readline())
for i in range(n):
    k=int(sys.stdin.readline())
    dp=[0 for _ in range(k+1)]
    for m in range(1,k+1):
        if m<=3:dp[m]+=1
        for n in range(1,4):
            if m-n>=0:
                dp[m]+=dp[m-n]
    print(dp[k])
