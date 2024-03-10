import sys
input = sys.stdin.readline
n, m = map(int,input().split()) #3<=n<=500,000 3<=m<=1,000,000
points = [[] for _ in range(n)]
visit=[0 for _ in range(n)]
parent = [i for i in range(n)]
idx = 0
def find_parent(x):
    if x==parent[x]:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

for i in range(m):
    a,b = map(int,input().split())
    points[a].append(b)
    points[b].append(a)
    a_ = find_parent(a)
    b_ = find_parent(b)
    if(idx==0):
        if(a_==b_):
            idx = i+1
        else:
            if(a_<b_):
                parent[b_] = a_
            else:
                parent[a_]=b_
print(idx)
