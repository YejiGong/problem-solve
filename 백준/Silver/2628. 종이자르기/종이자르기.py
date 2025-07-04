w, h = map(int,input().split())
n = int(input())
x_ = []
y_ = []
for _ in range(n):
    x,y = map(int,input().split())
    if x == 0:
        y_.append(y)
    else:
        x_.append(y)

x_.sort()
y_.sort()

nowx, maxx, nowy, maxy = 0,0,0,0

for i in x_:
    maxx = max(maxx, i-nowx)
    nowx = i

for i in y_:
    maxy = max(maxy, i-nowy)
    nowy = i

maxx = max(maxx, w-nowx)
maxy = max(maxy, h-nowy)
print(maxx*maxy)
