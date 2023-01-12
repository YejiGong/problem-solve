import sys

input = sys.stdin.readline
K=int(input())

width = []
height = []
total = []
for i in range(6):
    dir, len = map(int,input().split())
    total.append(len)
    if dir==1 or dir==2: #동, 서
        width.append(len)
    else:
        height.append(len)

maxar = max(height)*max(width)
maxhidx = total.index(max(height))
maxwidx = total.index(max(width))

smallf = abs(total[maxhidx-1] - total[(maxhidx+1)%6])
smalls = abs(total[maxwidx-1] - total[(maxwidx+1)%6])

area = maxar - (smallf * smalls)
print(area*K)