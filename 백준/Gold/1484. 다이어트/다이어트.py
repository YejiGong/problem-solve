G=int(input())
#G=cur**2 - past**2
res = []
past, cur = 1,2
while past<cur and cur+past<=G:
    tmp = cur**2-past**2
    if tmp==G:
        res.append(cur)
        past+=1
        cur+=1
    elif tmp<G:
        cur+=1
    else:
        past+=1
if res:
    for i in res:
        print(i)
else:
    print(-1)