import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
M, N = map(int,input().split())
graph=[]
for _ in range(M):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

dx=[1,-1,0,0]
dy=[0,0,-1,1]
dp=[[-1 for _ in range(N)] for _ in range(M)]

def dfs(x,y):
    if x==M-1 and y==N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    way = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[x][y]>graph[nx][ny]:
            way += dfs(nx,ny)
    dp[x][y] = way
    return dp[x][y]

print(dfs(0,0))