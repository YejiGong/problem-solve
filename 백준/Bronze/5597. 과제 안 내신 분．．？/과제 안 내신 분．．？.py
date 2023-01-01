import sys

input = sys.stdin.readline
arr=[i for i in range(1,31)]

for _ in range(28):
    tmp = int(input())
    if tmp in arr:
        arr.remove(tmp)

for i in arr:
    print(i)
