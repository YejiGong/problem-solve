import math
lenth = int(input())
r1, r2 = map(int,input().split())
b1, b2 = map(int,input().split())
y1, y2 = map(int,input().split())
coords=[[r1,r2], [b1,b2], [y1,y2]]
mid = 0
l, r = 0, lenth
def change(k,mid):
    return mid+abs(mid-k)

for i in range(3):
    x1,x2 = coords[i][0], coords[i][1]
    if x1!=x2:
        mid = (x1+x2)/2
        for j in range(i+1, 3):
            coords[j][0], coords[j][1] = change(coords[j][0], mid), change(coords[j][1], mid)
        l = change(l,mid)
        if l>r:
            r = l
        l = mid

result = r-l
result*=10
result=math.trunc(result)
result/=10
print("%.1f"%result)