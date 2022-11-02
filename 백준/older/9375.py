t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        m,n = map(str,input().split())
        if n in weardict:
            weardict[n].append(m)
        else:
            weardict[n] = [m]

    cnt = 1 

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)
