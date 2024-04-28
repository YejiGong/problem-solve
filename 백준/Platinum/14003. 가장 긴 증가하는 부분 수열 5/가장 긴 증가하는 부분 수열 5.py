import sys
from bisect import bisect_left
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))

dp_table=[-float('inf')]
store=[]

for i in L:
    if dp_table[-1]<i:
        dp_table.append(i)  
        store.append((len(dp_table)-1,i))
    else:
        pos=bisect_left(dp_table, i)
        dp_table[pos] = i
        store.append((pos,i))

index=len(dp_table)-1
print(index)

result=[]
for i in range(len(store)-1,-1,-1):
    if store[i][0]==index:
        result.append(store[i][1])
        index-=1

print(*result[::-1])