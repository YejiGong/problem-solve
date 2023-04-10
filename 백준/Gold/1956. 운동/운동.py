import sys
input = sys.stdin.readline
V, E = map(int,input().split())
INF = 10e9
graph=[[INF for _ in range(V+1)] for _ in range(V+1)]
4
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,V+1):
    for j in range(1,V+1):
            for k in range(1,V+1):
                    graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])


answer=INF
for i in range(1,V+1):
    answer = min(answer,graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)
