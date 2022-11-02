import sys
n,m=map(int,input().split())
input_=[[] for _ in range(n)]
sum_=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    input_[i]=list(map(int,sys.stdin.readline().split()))

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_[i][j]=sum_[i][j-1]+sum_[i-1][j]-sum_[i-1][j-1]+input_[i-1][j-1]

for i in range(m):
    x_1,y_1,x_2,y_2=map(int,sys.stdin.readline().split())
    result=sum_[x_2][y_2]-sum_[x_2][y_1-1]-sum_[x_1-1][y_2]+sum_[x_1-1][y_1-1]
    print(result)
