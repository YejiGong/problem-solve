k,n=map(int,input().split())
length=[]
for _ in range(k):
    length.append(int(input()))
end=max(length)
start=1

while(start<=end):
    mid=(start+end)//2
    cnt = 0
    for i in range(k):
        cnt+=length[i]//mid
    if cnt>=n:
        start=mid+1
    else:
        end=mid-1
print(end)
