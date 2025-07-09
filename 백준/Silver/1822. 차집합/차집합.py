import sys
input = sys.stdin.readline
A,B = map(int,input().split())
A_ = set(map(int,input().split()))
B_ = set(map(int,input().split()))
res = A_ - B_
print(len(res))
if(len(res)>0):
    res = list(res)
    res.sort()
    print(*res)