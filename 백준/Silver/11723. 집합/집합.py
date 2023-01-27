import sys
input = sys.stdin.readline

M = int(input())
S=set()
for i in range (M):
    tmp = input().split()
    if len(tmp)==1:
        if tmp[0] == "all":
            S = set([(i + 1) for i in range(20)])
        elif tmp[0] == "empty":
            S = set()
    else:
        tmp, num = tmp[0], int(tmp[1])
        if tmp=="add":
            if num not in S:
                S.add(num)
        elif tmp=="remove":
            S.discard(num)
        elif tmp=="check":
            if num in S:
                print(1)
            else:
                print(0)
        elif tmp=="toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)