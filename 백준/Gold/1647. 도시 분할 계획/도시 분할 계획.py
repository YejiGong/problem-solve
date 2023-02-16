import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph=[]
for _ in range(M):
    A,B,C = map(int,input().split())
    graph.append([C,A,B])

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0 for _ in range(N+1)]
for i in range(1,N+1):
    parent[i] = i

graph.sort()
selected = []
ans = 0
for C,A,B in graph:
    if find_parent(A) != find_parent(B):
        union_parent(A,B)
        ans += C
        selected.append(C)
ans -= selected.pop()
print(ans)


