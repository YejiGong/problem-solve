N,L,W,H=map(int,input().split())
left, right = 0, max(L,H,W)
for _ in range(100):
    mid = (left+right)/2
    cnt = (L//mid)*(W//mid)*(H//mid)
    if cnt>=N:
        left = mid
    else:
        right = mid

print("%.10f" %(right))
