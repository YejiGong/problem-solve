N,M = map(int,input().split())
books = list(map(int,input().split()))
books.sort()
visited=[0 for _ in range(N)]
cnt = 0
for i in range(N):
    if(books[i]>0):
        break
    if(visited[i]):
        continue
    cnt += 2*abs(books[i])

    for j in range(0,M):
        if i+j<N and books[i+j]<0:
            visited[i+j] = 1
for i in range(N-1,-1,-1):
    if(books[i]<0):
        break
    if(visited[i]):
        continue
    cnt += 2*abs(books[i])

    for j in range(0,M):
        if i-j>=0 and books[i-j]>0:
            visited[i-j] = 1
res = cnt - max(abs(books[0]), abs(books[-1]))
print(res)