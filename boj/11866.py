import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
queue=deque()
result_set=[]
for i in range(1,n+1):
    queue.append(i)
    
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result_set.append(queue.popleft())
print("<", end='')
for i in range(n-1):
    print(result_set[i],end=', ')
print(result_set[-1],end='')
print(">")
