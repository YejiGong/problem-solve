N,K = map(int,input().split())
res = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            tmp = ".".join([("0"+str(i))[-2:],("0"+str(j))[-2:]+("0"+str(k))[-2:]])
            if str(K) in tmp:
                res+=1
print(res)