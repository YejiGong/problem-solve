from collections import deque
N,K=map(int,input().split())
visit=[0 for _ in range(100001)]
dict= {}
visit[N]=1
queue=deque()
queue.append((N,0))
res = 0
while queue:
    x,t = queue.popleft()
    if(x==K):
        res = t
        break
    if x-1>=0 and visit[x-1]==0:
        visit[x-1]=1
        dict[x-1]=x
        queue.append((x-1,t+1))
    if x+1<=100000 and visit[x+1]==0:
        visit[x+1]=1
        dict[x+1]=x
        queue.append((x+1,t+1))
    if 2*x<=100000 and visit[2*x]==0:
        visit[2*x]=1
        dict[2*x]=x
        queue.append((2*x,t+1))
print(res)
t=K
arr = [t]
while t!=N:
    arr.append(dict[t])
    t = dict[t]
print(*reversed(arr))