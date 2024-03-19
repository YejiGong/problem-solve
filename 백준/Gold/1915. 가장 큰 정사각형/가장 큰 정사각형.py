import math
n,m=map(int,input().split())
graph = []
for _ in range(n):
    tmp = list(input())
    graph.append(list(int(i) for i in tmp))
dp=[[0 for _ in range(m)] for _ in range(n)]
dx=[0,-1,-1]
dy=[-1,-1,0]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            flag = True
            val = 1e9
            for k in range(3):
                nx = i+dx[k]
                ny = j+dy[k]
                if(0<=nx<n and 0<=ny<m and graph[nx][ny]==1):
                    val = min(val,dp[nx][ny])
                    continue
                else:
                    flag = False
                    break
            if flag==True:
                if(val!=1e9):
                    dp[i][j] = max(2,int(val+1)) #2x2짜리 사각형이 있다.
                else:
                    dp[i][j] = 2
            else:
                dp[i][j] = 1 #자기자신
maxVal = max(list(max(dp[i]) for i in range(n)))
print((maxVal)**2)