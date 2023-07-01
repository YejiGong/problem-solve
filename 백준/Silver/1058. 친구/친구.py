import sys
input = sys.stdin.readline
N=int(input())
graph=[[1 if i=='Y' else -1 for i in input()] for _ in range(N)]
visited = [[0 for i in range(N)] for _ in range(N)]
max_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[i][j]==-1:
            continue
        else:
            cnt += 1 #친구이므로 cnt 추가 -> i,j가 친구 : j의 친구를 찾기
            visited[i][j]=1
            for k in range(N):
                if k!=i and graph[i][k]==-1 and graph[j][k]==1 and visited[i][k]==0:
                    cnt+=1
                    visited[i][k]=1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)
