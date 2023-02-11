import sys
import heapq
input=sys.stdin.readline
N, M = map(int,input().split())
graph=[[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
ans=[]
queue=[]
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B) #B번 문제보다 A번을 먼저 푸는 것이 좋다
    inDegree[B]+=1

for i in range(1,N+1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i]-=1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)

print(*ans)

