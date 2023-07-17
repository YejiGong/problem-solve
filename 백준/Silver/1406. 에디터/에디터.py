import sys
input = sys.stdin.readline
strs = list(input().strip())
strs2=[]
M = int(input())
commands = [input().strip() for _ in range(M)]
cursor = len(strs)
for i in commands:
    if i[0]=='P':
        strs.append(i.split()[1])
    elif i=='L':
        if strs:
            strs2.append(strs.pop())
    elif i=='D':
        if strs2:
            strs.append(strs2.pop())
    elif i=='B':
        if strs:
            strs.pop()

print(''.join(strs + list(reversed(strs2))))