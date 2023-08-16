import sys
input = sys.stdin.readline
T=int(input())
def find_parent(parent,x):
    result = [x]
    while parent[x]:
        result.append(parent[x])
        x = parent[x]
    return result

for _ in range(T):
    N = int(input())
    parent=[0]*(N+1)
    for _ in range(N-1):
        a,b = map(int,input().split())
        parent[b] = a
    a, b= map(int,input().split())
    a_parent = find_parent(parent,a)
    b_parent = find_parent(parent,b)

    i,j =0,0
    if len(a_parent)>len(b_parent):
        i = len(a_parent) - len(b_parent)
    else:
        j = len(b_parent) - len(a_parent)

    while a_parent[i] != b_parent[j]:
        i+=1
        j+=1
    print(a_parent[i])

