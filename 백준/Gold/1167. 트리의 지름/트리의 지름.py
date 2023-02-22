import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
V=int(input())
graph=[[] for _ in range(V+1)]
for i in range(V-1):
    tmp = list(map(int,input().split()))
    tmp=tmp[:-1]
    a=tmp[0]
    for j in range(1,(len(tmp)-1),2):
        b, c = tmp[j], tmp[j+1]
        graph[a].append((b,c))
        graph[b].append((a,c))

def dfs(x,w):
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a,w+b)

distance=[-1]*(V+1)
distance[1]=0
dfs(1,0)

start = distance.index(max(distance)) #가장 가중치가 큰 노드 찾기
distance=[-1]*(V+1)
distance[start] = 0
dfs(start,0) #가장 가중치가 큰 노드를 기준으로 가장 먼 노드 찾기

print(max(distance))


