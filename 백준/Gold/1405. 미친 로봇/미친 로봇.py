import copy
n,E,W,S,N = map(int,input().split())
percent = [E,W,S,N]
visited=[[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0

def track(x,y,cnt,pct):
    global result
    visited[x][y]=1
    if cnt<n:
        for dir in range(4):
            nx,ny = x+dx[dir], y+dy[dir]
            if visited[nx][ny]!=1:
                track(nx,ny,cnt+1,pct*(percent[dir]/100))
                visited[nx][ny]=0
    else:
        result+=pct
        return

track(n,n,0,1)
print(result)