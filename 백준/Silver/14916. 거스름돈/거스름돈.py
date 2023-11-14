n=int(input())
i = 0
ans = 1e9
while(True):
    tmp = 5*i
    if tmp>n:
        break
    elif(tmp+2*((n-tmp)//2)==n):
        ans = min(ans,i + (n-tmp)//2)
    i+=1

if(ans==1e9):
    print(-1)
else:
    print(ans)