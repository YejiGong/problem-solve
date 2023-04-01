import sys
input = sys.stdin.readline
N,M=map(int,input().split())
INF = 1e9
edges=[]
distance = [INF] * (N+1)
for _ in range(M):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))

def bellman_ford(start):
    distance[start]=0
    for i in range(N): #모든 노드
        for j in range(M): #모든 간선
            cur, nxt, cost = edges[j][0], edges[j][1], edges[j][2]
            if distance[cur] != INF and distance[nxt]>distance[cur]+cost:
                distance[nxt] = distance[cur]+cost
                if i==N-1: #마지막에서도 값이 갱신 -> 음수 순환이 존재.
                    return True
    return False

cycle = bellman_ford(1)

if cycle:
    print("-1")
else:
    for i in range(2,N+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])