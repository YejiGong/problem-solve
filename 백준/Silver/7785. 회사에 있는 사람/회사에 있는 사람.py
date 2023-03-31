import sys
input=sys.stdin.readline
n= int(input())
log={}
for _ in range(n):
    name, state = map(str, input().split())
    if state=="enter":
        log[name]=state
    else:
        del log[name]
sorted_log = sorted(log.keys(), reverse=True)
for i in sorted_log:
    print(i)