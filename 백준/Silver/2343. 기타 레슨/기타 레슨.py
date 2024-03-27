N,M = map(int,input().split())
lecture = list(map(int,input().split()))
left,right = max(lecture),sum(lecture)
ans = 0
while left<=right:
    mid = (left+right)//2
    cnt = 1
    tmp = 0
    for t in lecture:
        if t+tmp>mid:
            cnt+=1
            tmp = 0
        tmp+=t
    if cnt<=M:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
        