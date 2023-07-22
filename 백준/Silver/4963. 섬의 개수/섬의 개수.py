import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x,y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w and visited[nx][ny]==0 and maps[nx][ny]==1:
            visited[nx][ny] = 1
            dfs(nx,ny)


dx=[1,1,1,0,-1,-1,-1,0]
dy=[-1,0,1,1,1,0,-1,-1]
while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break
    else:
        maps = [list(map(int,input().split())) for _ in range(h)]
        visited = [[0 for _ in range(w)] for _ in range(h)]
        #1 = Land, 0=Sea
        result = 0
        for i in range(h):
            for j in range(w):
                if maps[i][j]==1 and visited[i][j]==0:
                    visited[i][j]=1
                    result+=1
                    dfs(i,j)
        print(result)
