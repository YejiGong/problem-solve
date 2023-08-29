import sys
input=sys.stdin.readline
N=int(input())
players=[input() for _ in range(N)]
tmp={}
players.sort()
for i in players:
    if i[0] in tmp.keys():
        tmp[i[0]]+=1
    else:
        tmp[i[0]]=1
flag = False
for i in tmp.keys():
    if tmp[i]>=5:
        flag = True
        print(i,end='')
if(flag==False):
    print("PREDAJA")