N=int(input())
start, end=0,N
while start<end:
    mid= (start+end)//2
    if mid**2==N:
        print(mid)
        break
    else:
        if mid**2<N:
            start = mid
        else:
            end = mid