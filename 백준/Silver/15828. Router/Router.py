from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
packets=deque()
while(True):
    p = int(input())
    if p==-1:
        break
    if p!=0:
        if len(packets)<n:
            packets.append(p)
    else:
        packets.popleft()

if len(packets)==0:
    print("empty")
else:
    print(*packets)

