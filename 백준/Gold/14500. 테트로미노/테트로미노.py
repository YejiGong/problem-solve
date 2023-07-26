import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def find(x,y,sum,l):
    global ans
    if l == 4 :
        ans = max(ans, sum)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]!=1:
            visited[nx][ny] = 1
            find(nx,ny,sum+paper[nx][ny],l+1)
            visited[nx][ny] = 0


def find_else(x, y):
    global ans
    for i in range(4):
        tmp = paper[x][y]
        for j in range(3):
            t = (i+j)%4
            nx = x+dx[t]
            ny = y+dy[t]

            if 0<=nx<N and 0<=ny<M:
                tmp += paper[nx][ny]
            else:
                tmp = 0
                break
        ans = max(ans, tmp)

ans = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        find(i,j,paper[i][j],1)
        visited[i][j]=0
        find_else(i,j)
print(ans)