N= int(input())
nums = list(map(int,input().split()))
res,t,s = 0,0,0
for i in range(N):
    x = nums[i]
    res += t+ 2*s + x
    t += 2*s + x
    s += x
    print(res, end=' ')