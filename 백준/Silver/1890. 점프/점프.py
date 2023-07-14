import sys
input = sys.stdin.readline
N= int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
dp=[[0 for _ in range(N)] for _ in range(N)]
dx = [1,0]
dy = [0,1]
dp[0][0]=1
for i in range(N):
    for j in range(N):
        for k in range(2):
            nx = i + dx[k]*graph[i][j]
            ny = j + dy[k]*graph[i][j]

            if 0<=nx<N and 0<=ny<N and (i!=N-1 or j!=N-1):
                dp[nx][ny] += dp[i][j]

print(dp[N-1][N-1])