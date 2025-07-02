N = int(input())
if(N==1):
    print(1)
else:
    l,r = 1,2
    cnt = 1
    while l<r and r<N:
        tmp = (l+r) * (r-l+1)//2
        if tmp==N:
            cnt += 1
            l += 1
            r += 1
        else:
            if tmp<N:
                r += 1
            else:
                l += 1
    print(cnt)