n=int(input())
a,b = map(int,input().split()) #촌수 계산해야하는 사람
m = int(input()) #부모 자식간의 관계의 개수
graph = [[] for i in range(n+1)]
result = []
for _ in range(m):
    x,y = map(int,input().split()) #부모-자식
    graph[x].append(y)
    graph[y].append(x)
visit = [0 for i in range(n+1)]

def dfs(v,num):
    num += 1
    visit[v] = 1

    if v==b:
        result.append(num)
    for i in graph[v]:
        if visit[i]==0:
            dfs(i,num)

dfs(a,0)

if len(result)==0:
    print(-1)
else:
    print(result[0]-1)
