import sys
from collections import deque
input = sys.stdin.readline
T=int(input().rstrip())

for _ in range(T):
    N,K = map(int,input().split())
    time = list(map(int,input().split()))
    graph=[[] for _ in range(N+1)]
    topology = [0] * (N+1)
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        topology[b]+=1
    W=int(input().rstrip())
    queue = deque()
    dp=[0 for _ in range(N+1)]
    for i in range(1,N+1):
        if topology[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]

    while queue:
        cnt = queue.popleft()
        for i in graph[cnt]:
            topology[i]-=1
            dp[i] = max(dp[i], dp[cnt]+time[i-1])
            if topology[i]==0:
                queue.append(i)

    print(dp[W])


