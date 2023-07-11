import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,K = map(int,input().split())
graph=[[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
garbages = []
for _ in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1
    garbages.append((r-1,c-1))

dirx=[0,0,1,-1]
diry=[1,-1,0,0]

def dfs(x,y):
    global N,M
    cnt = 0
    for i in range(4):
        dx=x+dirx[i]
        dy=y+diry[i]
        if 0<=dx<N and 0<=dy<M and graph[dx][dy]==1 and visited[dx][dy]==0:
            cnt+=1
            visited[dx][dy]=1
            cnt+=dfs(dx,dy)
    return cnt

result = 0
for i in garbages:
    result = max(result,dfs(i[0],i[1]))

print(result)