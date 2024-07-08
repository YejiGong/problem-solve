from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
table = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    table[B].append(A)
    #B 해킹 -> A 해킹

def bfs(x):
    queue = deque([x])
    visit=[0]*(N+1)
    visit[x] = 1
    cnt = 1
    while queue:
        t = queue.popleft()
        for i in table[t]:
            if not visit[i]:
                queue.append(i)
                visit[i] = 1
                cnt +=1
    return cnt

max_cnt = 0
res=[]
for i in range(1,N+1):
    result = bfs(i)
    if result > max_cnt:
        max_cnt = result
        res.clear()
        res.append(i)
    elif result == max_cnt:
        res.append(i)

print(*res)