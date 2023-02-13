import sys
input = sys.stdin.readline
R, C = map(int,input().split())
alph = [list(map(lambda x: ord(x)-65,input().rstrip())) for _ in range(R)]
visited=[0]*26
cnt = 1
visited[alph[0][0]]=1
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,z):
    global cnt
    cnt = max(cnt,z) #최대 칸 초기화
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and visited[alph[nx][ny]]==0:
            visited[alph[nx][ny]]=1
            dfs(nx,ny,z+1)
            visited[alph[nx][ny]]=0
    return cnt
print(dfs(0,0,cnt))