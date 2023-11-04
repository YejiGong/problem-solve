N,L=map(int,input().split())
def sum_(n,m):
    result = 0
    for i in range(n,m+1):
        result+=i
    return result
val = L-1
while(val<=100):
    x = (N-((val-1)*val//2))/val
    if x>0 and x == int(x):
        x = int(x)
        if(val==L-1 and x==1):
            print(" ".join(map(str,list(i for i in range(x-1,x+val)))))
            exit()
        elif(val>=L):
            print(" ".join(map(str, list(i for i in range(x,x+val)))))
            exit()
    val+=1


print(-1)