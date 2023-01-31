from collections import deque
MAX=100001
dist = [-1]*MAX

N, K = map(int,input().split())
q = deque()
q.append(N)
dist[N]=0

while q:
    x = q.popleft()
    if x==K:
        break
    for i in (x+1, x-1,2*x):
        if 0<=i<=100000 and dist[i]==-1:
            if i==2*x:
                q.appendleft(i)
                dist[i] = dist[x]
            else:
                q.append(i)
                dist[i] = dist[x]+1

print(dist[K])