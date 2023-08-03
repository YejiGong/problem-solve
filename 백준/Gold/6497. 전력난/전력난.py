import sys
input =sys.stdin.readline

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

while True:
    m, n = map(int,input().split())
    if(m==0 and n==0):
        break
    else:
        parent = [i for i in range(m+1)]
        sum_cost = 0
        graph =[]
        for _ in range(n):
            x,y,z = map(int,input().split())
            sum_cost+=z
            graph.append((z,x,y))
        graph.sort(key=lambda x:x[0])

        answer = 0

        for cost, a, b in graph:
            if not same_parent(a,b):
                union_parent(a,b)
                answer += cost

        print(sum_cost-answer)
