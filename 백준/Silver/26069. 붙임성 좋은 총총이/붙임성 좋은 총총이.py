import sys
input = sys.stdin.readline
n= int(input())
meets = [list(map(str,input().split())) for _ in range(n)]
queue = ["ChongChong"]
for a,b in meets:
    if a in queue and b not in queue:
        queue.append(b)
    elif b in queue and a not in queue:
        queue.append(a)

print(len(queue))