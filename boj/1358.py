def calc(x,y,a,b):
    return (x-a)**2+(b-y)**2
w,h,x,y,p=map(int,input().split())
prob=0
r=(h/2)**2
for _ in range(p):
    x_,y_ = map(int,input().split())
    if(x<=x_ and x_<=x+w and y<=y_ and y_<=y+h):
        prob+=1
    elif(calc(x,y+(h/2),x_,y_)<=r):
        prob+=1
    elif(calc(x+w, y+(h/2), x_, y_)<=r):
        prob+=1

print(prob)

