import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    heap=[]
    heapq.heappush(heap, [0,start])
    d = [INF for _ in range(n+1)]
    d[start] = 0

    while heap:
        tmp = heapq.heappop(heap)
        cost = tmp[0]
        node = tmp[1]

        if cost>d[node]:
            continue
        for i in graph[node]:
            v = i[0]
            n_cost = d[node] + i[1]

            if n_cost<d[v]:
                d[v] = n_cost
                heapq.heappush(heap, [n_cost, v])
    
    return d


INF = 1e9
T= int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph=[[] for _ in range(n+1)]
    destination_candidate=[]


    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    for _ in range(t):
        x = int(input())
        destination_candidate.append(x)

    start_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    ans = []

    for i in destination_candidate:
        if start_[g]+g_[h]+h_[i] == start_[i] or start_[h]+h_[g]+g_[i] == start_[i]:
            ans.append(i)
    ans.sort()
    print(*ans)
