import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
sums=[0 for _ in range(n)]
sums[0]=nums[0]
for i in range(1,n):
    sums[i]=sums[i-1]+nums[i]

for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if(i>1):
        print(sums[j-1]-sums[i-2])
    else:
        print(sums[j-1])
