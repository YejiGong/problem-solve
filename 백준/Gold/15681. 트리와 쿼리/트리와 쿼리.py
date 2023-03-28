import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q = map(int,input().split())
tree=[[] for _ in range(N+1)]
count=[0 for _ in range(N+1)]
def count_tree(x):
    count[x] = 1
    for i in tree[x]:
        if not count[i]:
            count_tree(i)
            count[x] += count[i]

for _ in range(N-1):
    U, V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

count_tree(R)

for _ in range(Q):
    U = int(input())
    print(count[U])

