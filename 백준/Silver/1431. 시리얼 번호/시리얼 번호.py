import sys
input = sys.stdin.readline
N=int(input())
serials = [input().rstrip() for _ in range(N)]

def sum_(s):
    tmp = 0
    for i in s:
        if i.isdigit():
            tmp+=int(i)
    return tmp

serials.sort(key=lambda x:(len(x), sum_(x), x))
for s in serials:
    print(s)
