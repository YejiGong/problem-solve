import sys
input=sys.stdin.readline
n=int(input())
x,y=[],[]
for _ in range(n):
    x_,y_ = map(int,input().split())
    x.append(x_)
    y.append(y_)
x,y = x+[x[0]], y+[y[0]]

ans=0
for i in range(n):
    ans+=(x[i]*y[i+1])-(x[i+1]*y[i])
    
print(round(abs(ans)/2,1))
