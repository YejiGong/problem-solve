import sys

num = int(sys.stdin.readline())
sum = 1
for i in range(num):
    tmp = int(sys.stdin.readline())
    sum+=tmp

print(sum-num)