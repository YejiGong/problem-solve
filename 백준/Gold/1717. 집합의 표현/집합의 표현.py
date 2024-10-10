import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
parent = [i for i in range(n+1)]
def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
        return parent[x]
    else:
        return parent[x]
def union(x,y):
    parent_x = get_parent(x)
    parent_y = get_parent(y)
    if x<y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

for _ in range(m):
    a,b,c = map(int,input().split())
    if a==1: #확인
        if get_parent(b) == get_parent(c):
            print('YES')
        else:
            print('NO')
    else: #합집합
        union(b,c)
