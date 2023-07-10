import re
T=int(input())
r = re.compile('(100+1+|01)+')
for _ in range(T):
    tmp = input()
    if r.fullmatch(tmp):
        print("YES")
    else:
        print("NO")