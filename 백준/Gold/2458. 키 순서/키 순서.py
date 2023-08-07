import sys
input = sys.stdin.readline
N,M=map(int,input().split())
stud = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    stud[a][b]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if stud[i][j] ==1 or (stud[i][k]==1 and stud[k][j]==1):
                stud[i][j]=1

ans = 0
for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        tmp += stud[i][j]+stud[j][i]
    
    if tmp==N-1:
        ans+=1

print(ans)
