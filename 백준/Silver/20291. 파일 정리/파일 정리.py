import sys

N=int(input())
dict={}
keys=[]
for _ in range(N):
    tmp = input().split(".")[1]
    if tmp in dict:
        dict[tmp]+=1
    else:
        dict[tmp]=1
        keys.append(tmp)
keys.sort()

for i in keys:
    print(i, dict[i])