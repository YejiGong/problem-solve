import sys
input = sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
graph=[[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1 #a가 b보다 무겁다

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        if i!=j and not graph[i][j] and not graph[j][i]:
            tmp +=1
    print(tmp)