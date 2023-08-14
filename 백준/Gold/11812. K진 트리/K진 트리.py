import sys
input = sys.stdin.readline
N, K, Q = map(int,input().split())

for _ in range(Q):
    x, y= map(int,input().split())

    if K==1:
        print(abs(x-y))
        continue

    cnt=0
    while(y!=x):
        while (x>y):
            cnt += 1
            x = (x+K - 2) // K
        while(y>x):
            cnt+=1
            y = (y+K-2)//K

    print(cnt)




