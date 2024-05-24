def getSum(n):
    result = 0
    tmp = 10
    while n>=1:
        cnt = n%tmp
        n//=tmp
        result += cnt
    return result

N=int(input())
for _ in range(N):
    tmp = int(input())
    res = getSum(tmp)
    if(res%2==1):
        print(tmp)
    else:
        cnt = 9
        flag=False
        while tmp*cnt<=10**18:
            res = getSum(tmp*cnt)
            if(res%2==1):
                print(tmp*cnt)
                flag=True
                break
            else:
                cnt *= 10
                cnt += 9
        if(flag==False):
            print(-1)

