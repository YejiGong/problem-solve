import sys
N = int(sys.stdin.readline())
rank = sorted([int(sys.stdin.readline()) for _ in range(N)])
cnt = 0 
for i in range(N):
    if rank[i] != i+1:
        cnt += abs(rank[i]-(i+1))
print(cnt)