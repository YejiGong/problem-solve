X,Y = map(int,input().split())
X_ = X/Y
N= int(input())
prices = [list(map(int,input().split())) for _ in range(N)]
min_price = X_
for x,y in prices:
    x = x/y
    if(x<min_price):
        min_price = x
print("%.2f" % (min_price*1000))
