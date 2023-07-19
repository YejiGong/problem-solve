import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N=int(input())
graph=[[[0 for _ in range(101)] for _ in range(N)] for _ in range(N)]
max_num = 0
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        graph[i][j][0] = tmp[j]
    max_num = max(max_num, max(tmp))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def dfs(depth,x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny][depth+1] ==1:
            graph[nx][ny][depth+1] = -1
            dfs(depth,nx,ny)
    return 1

def check(depth):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0]>depth:
                graph[i][j][depth+1] = 1
    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j][depth+1]==1:
                graph[i][j][depth+1]=-1
                result+=1
                dfs(depth,i,j)

    return result

answer = 0
for i in range(max_num):
    answer = max(answer, check(i))
print(answer)