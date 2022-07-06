n, m, k = map(int,input().split())

def square(n, m, c):
    if (m==1):
        return n%c
    
    k=square(n,m//2,c)
    
    if(m%2==0):
        return (k*k)%c
    else:
        return (k*k*n)%c

tmp=square(n,m,k)
print(tmp)
