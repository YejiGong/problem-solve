M=int(input())
cups=[0 for _ in range(4)]
cups[1] = 1
for _ in range(M):
    X,Y = map(int,input().split())
    if(cups[X]==1):
        cups[Y]=1
        cups[X]=0
    elif(cups[Y]==1):
        cups[X]=1
        cups[Y]=0
for i in range(1,4):
    if(cups[i]==1):
        print(i)