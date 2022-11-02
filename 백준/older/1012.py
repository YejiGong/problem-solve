import sys
sys.setrecursionlimit(10000)

t=int(input())

def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<m:
            if case[nx][ny]==1:
                case[nx][ny]=0
                dfs(nx,ny)
    
for _ in range(t):
    m,n,k=map(int,input().split())
    case=[[0]*m for i in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        case[y][x]=1
    result=0
    for i in range(n):
        for j in range(m):
            if case[i][j]>0:
                dfs(i,j)
                result+=1
    print(result)
