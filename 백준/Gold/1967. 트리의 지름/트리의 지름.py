import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(x,w):
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a,w+b)

distance=[-1]*(n+1)
distance[1]=0
dfs(1,0)

start = distance.index(max(distance)) #가장 가중치가 큰 노드 찾기
distance=[-1]*(n+1)
distance[start] = 0
dfs(start,0) #가장 가중치가 큰 노드를 기준으로 가장 먼 노드 찾기

print(max(distance))
