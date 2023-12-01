from collections import deque
N=int(input())
parent = list(map(int,input().split()))
nodes=[[] for _ in range(N)]
num = int(input())
visit = [0 for _ in range(N)]
for idx in range(N):
    if parent[idx]!=-1:
        nodes[parent[idx]].append(idx)
queue = deque()
queue.append(num)
visit[num]=1
while queue:
    x = queue.popleft()
    for i in nodes[x]:
        if visit[i]==0:
            queue.append(i)
            visit[i]=1

def check_leaf_node(idx):
    for i in nodes[idx]:
        if visit[i]==0:
            return False
    return True
res = 0
for idx in range(N):
    if check_leaf_node(idx) and (visit[idx]==0):
        res+=1
print(res)