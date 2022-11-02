n=int(input())
f=[0 for _ in range(n+1)]
f[1]=1
f[2]=1
rec_cnt=1
dp_cnt=0
def rec_fib(n):
    global rec_cnt
    if n==1 or n==2:
        return 1
    else:
        rec_cnt+=1
        return rec_fib(n-1)+rec_fib(n-2)
    
def dp_fib(n):
    global dp_cnt
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        dp_cnt+=1
    return f[n]

rec_fib(n)
dp_fib(n)

print(rec_cnt, dp_cnt)
