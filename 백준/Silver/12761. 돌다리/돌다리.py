from collections import deque
A,B,N,M = map(int,input().split())
stones = [0 for _ in range(100001)]
stones[N] = 1
#동규는 N번, 주미는 M번 위에 있음.
#+-1, +-A,+-B, N*A,N*B
queue = deque([(N,0)])
dplus=[1,-1,A,-A,B,-B]
dmult=[A,B]
while(N!=M):
    cnt, n = queue.popleft()
    N = cnt
    if(cnt==M):
        print(n)
        break
    diff = M-cnt
    for i in range(8):
        if(i<6):
            nx = cnt+dplus[i]
        else:
            nx = cnt*dmult[i-6]
        if(0<=nx<=100000 and stones[nx]==0):
            stones[nx]=1
            queue.append((nx,n+1))
