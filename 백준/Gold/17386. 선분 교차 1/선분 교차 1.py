x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
if(x1>x2):
    x1,x2 = x2,x1
    y1,y2 = y2,y1
if(x3>x4):
    x3,x4 = x4,x3
    y3,y4 = y4,y3
#L1: (x1,y1) <-> (x2,y2)
#L2: (x3,y3) <-> (x4,y4)

if(x2!=x1 and x4!=x3):
    m1 = (y2-y1)/(x2-x1)
    m2 = (y4-y3)/(x4-x3)
    if(m1!=m2):
        x_cor = (m1 * x1 - y1 - m2 * x3 + y3) / (m1 - m2)
        if(x1<=x_cor<=x2 and x3<=x_cor<=x4):
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    #하나 or 둘 다 가 수직임.
    if(x2==x1 and x3==x4):
        if(x2==x3): #동일한 수직선
            print(1)
        else:
            print(0) #둘 다 수직, 만날 수 없다.
    else:
        if(x2==x1): #L1이 수직
            m2 = (y4 - y3) / (x4 - x3)
            if(x3<=x2<=x4 and y1<=m2*(x2-x3)+y3<=y2): #L2의 범위가 L1 수직을 지나가고, L2에서 L1 수직 x의 교점이 L1의 범위 이내다.
                print(1)
            else:
                print(0)
        elif(x3==x4): #L2가 수직
            m1 = (y2 - y1) / (x2 - x1)
            if(x1<=x3<=x2 and y3<=m1*(x3-x1)+y1<=y4):
                print(1)
            else:
                print(0)