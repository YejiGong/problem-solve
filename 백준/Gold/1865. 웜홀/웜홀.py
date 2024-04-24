import sys
input=sys.stdin.readline
INF=int(1e9)
def bf(start): #벨만포드
    dis=[INF]*(n+1)
    dis[start]=0
    
    for i in range(n):
        for edge in edges:
            cur=edge[0]
            next_node=edge[1]
            cost=edge[2]
            
            if dis[next_node]>cost+dis[cur]:
                dis[next_node]=cost+dis[cur]
                if i==n-1:
                    print("YES")
                    return
    print("NO")
    return

tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    edges=[]
    for _ in range(m):
        s,e,t=map(int,input().split()) #도로
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s,e,t=map(int,input().split()) #웜홀
        edges.append((s,e,-t))
    
    key=bf(1)