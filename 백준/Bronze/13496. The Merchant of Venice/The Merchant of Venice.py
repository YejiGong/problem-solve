n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    cnt = 0
    for j in range(a):
        t,p = map(int,input().split())
        if(c*b >= t):
            cnt = cnt + p
    format_ = f"Data Set {i+1}:"
    print(format_); print(cnt); print();