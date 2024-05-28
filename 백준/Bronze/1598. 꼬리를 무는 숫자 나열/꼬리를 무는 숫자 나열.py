a,b = map(int,input().split())
a_x = a//4
a_y = a%4
b_x = b//4
b_y = b%4
if a_y==0 :
    a_y = 4
    a_x -= 1
if b_y==0 :
    b_y = 4
    b_x -=1
print(abs(a_x-b_x) + abs(a_y-b_y))