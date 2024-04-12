import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split()) #v:정점, e:간선
k = int(input()) #시작 정점
graph=[[]*(v+1) for _ in range(v+1)]
for i in range(e):
    x,y,w = map(int,input().split())
    graph[x].append((y,w)) #u->v 간선 가중치 w.

distance = [INF]*(v+1) #초기값

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(k)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])