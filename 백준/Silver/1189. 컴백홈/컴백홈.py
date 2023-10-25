R,C,K = map(int,input().split())
graph=[list(map(str,input())) for _ in range(R)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
x,y=R-1,0
visited=[[0 for _ in range(C)] for _ in range(R)]
result = 0
def dfs(x,y,depth):
    global result
    visited[x][y]=1
    if x==0 and y==C-1 and depth==K:
        result+=1
        return;
    for i in range(4):
        nx = x +dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and visited[nx][ny]==0 and graph[nx][ny]!='T':
            visited[nx][ny]=1
            dfs(nx,ny,depth+1)
            visited[nx][ny]=0

dfs(x,y,1)
print(result)