from collections import deque
F,S,G,U,D = map(int,input().split())
visit=[0 for _ in range(F+1)]
queue = deque()
queue.append((S,0))
visit[S]=1
result = -1
while queue:
    x,num = queue.popleft()
    if x==G:
        result = num
        break
    if x+U<=F and visit[x+U]==0:
        visit[x+U]=1
        queue.append((x+U,num+1))
    if x-D>0 and visit[x-D]==0:
        visit[x-D]=1
        queue.append((x-D,num+1))

if(result==-1):
    print("use the stairs")
else:
    print(result)
