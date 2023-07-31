import sys
input = sys.stdin.readline
N= int(input())
M= int(input())
arr = []
parent = [i for i in range(N+1)]
def find(a):
    if a ==parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = b
    else:
        parent[b] = a
for _ in range(M):
    a,b,c = map(int,input().split())
    arr.append((c,a,b))
res = 0
arr.sort(key=lambda x: x[0])
for dis, a, b in arr:
    if find(a) != find(b):
        union(a,b)
        res += dis
print(res)