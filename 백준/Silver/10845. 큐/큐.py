import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
queue=deque()
for _ in range(N):
    order=input().split()
    if order[0]=="push":
        n=int(order[1])
        queue.append(n)
    elif order[0]=="pop":
        if len(queue)>0:
            print(queue.popleft())
        else:
            print("-1")
    elif order[0]=="size":
        print(len(queue))
    elif order[0]=="empty":
        if len(queue)>0:
            print("0")
        else:
            print("1")
    elif order[0]=="front":
        if len(queue)>0:
            print(queue[0])
        else:
            print("-1")
    elif order[0]=="back":
        if len(queue)>0:
            print(queue[-1])
        else:
            print("-1")