import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
img = [[i for i in input()]for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    default = img[x][y]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and img[nx][ny]==default and visited[nx][ny]==0:
            visited[nx][ny]=1
            dfs(nx,ny)

def dfs_2(x,y):
    default = img[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and (img[nx][ny] == default or (default=='G' and img[nx][ny]=='R') or (default=='R' and img[nx][ny]=='G')) and visited_2[nx][ny] == 0:
            visited_2[nx][ny] = 1
            dfs_2(nx, ny)

visited=[[0 for _ in range(N)]for _ in range(N)]
visited_2 =[[0 for _ in range(N)] for _ in range(N)]

result_1 = 0
result_2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            visited[i][j]=1
            result_1+=1
            dfs(i,j)
        if visited_2[i][j]==0:
            visited_2[i][j]=1
            result_2+=1
            dfs_2(i,j)

print(result_1, result_2)
