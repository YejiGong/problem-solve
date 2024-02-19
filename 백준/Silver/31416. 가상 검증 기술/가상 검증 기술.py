Q=int(input())
for _ in range(Q):
    ta,tb,va,vb = map(int,input().split())
    timeB = tb*vb
    timeA = ta*(timeB//ta)
    va -= (timeB//ta)
    while va>0:
        va-=1
        if timeA>timeB:
            timeB+=ta
        else:
            timeA+=ta

    print(max(timeA,timeB))