import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    n=int(input())
    cnt=0
    for j in range(n):
        cx, cy, r = map(int,input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        pow_r = r**2
        if pow_r>dis1 and pow_r>dis2:
            pass
        elif pow_r>dis1:
            cnt+=1
        elif pow_r>dis2:
            cnt+=1
    print(cnt)