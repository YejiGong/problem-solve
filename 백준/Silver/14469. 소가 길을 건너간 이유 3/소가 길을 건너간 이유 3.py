N = int(input())
times=[list(map(int,input().split())) for _ in range(N)]
times.sort(key = lambda x:x[0])
time = 0
for a,b in times:
    if a<time:
        a = time
    time = a + b
print(time)