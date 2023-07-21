N=int(input())
names = [[i for i in input()] for _ in range(N)]
lenth=len(names[0])
check=[0 for _ in range(lenth)]
for i in range(1,N):
    for j in range(lenth):
        if names[i][j] != names[i-1][j]:
            check[j]=1

for i in range(lenth):
    if check[i]==0:
        print(names[0][i], end='')
    else:
        print('?',end='')
