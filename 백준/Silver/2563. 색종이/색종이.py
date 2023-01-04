import sys
input = sys.stdin.readline

n = int(input())
papers=[[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    p,q = map(int,input().split())
    for i in range(p, p+10):
        for j in range(q, q+10):
            papers[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if papers[i][j]==1:
            cnt+=1

print(cnt)