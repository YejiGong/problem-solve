import sys
n, m = map(int,sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().split()))
start=1
end=max(trees)
result=0
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in trees:
        if i>mid:
            cnt+=i-mid

    if cnt>=m:
        start=mid+1
    else:
        end=mid-1
print(end)
