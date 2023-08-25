N,K=map(int,input().split())
nums=list(map(int,input().split(",")))
tmp=nums
for i in range(K):
    tmp=[0 for _ in range(N-i-1)]
    for j in range(N-i-1):
        tmp[j]=nums[j+1]-nums[j]
    nums=tmp
if tmp:
    for i in tmp[:-1]:
        print(i,end=",")
    print(tmp[-1])
