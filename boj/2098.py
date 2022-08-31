import sys
input=sys.stdin.readline
import sys
input=sys.stdin.readline
n=int(input())
graph=[]
INF=float('inf')
dp=[[None]*(1<<n) for _ in range(n)]

for _ in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

def solve(cur,visited):
    if visited == ((1<<n) -1) : #all visited
        return graph[cur][0] or INF
    
    if dp[cur][visited] is not None:
        return dp[cur][visited]
    
    min_dist = INF
    
    for i in range(n):
        if not visited & (1<<i) and graph[cur][i] != 0:
            min_dist = min(min_dist, graph[cur][i]+solve(i, visited | (1<<i)))
        
    dp[cur][visited] = min_dist
    return min_dist

print(solve(0,1))
