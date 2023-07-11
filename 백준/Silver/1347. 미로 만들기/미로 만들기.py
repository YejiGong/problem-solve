N=int(input())
trace=[i for i in input()]
diry=[0,1,0,-1]
dirx=[1,0,-1,0]
#남동북서
check=[(0,0)]
x,y=0,0
min_x,min_y = 0,0
max_x,max_y = 0,0
dir=0
for i in trace:
    if i=="L":
        dir=(dir+1)%4
    elif i=="R":
        dir=(dir-1)%4
    elif i=="F":
        x+=dirx[dir]
        y+=diry[dir]
        check.append((x,y))
        min_x,min_y = min(min_x,x), min(min_y,y)
        max_x, max_y = max(max_x,x), max(max_y,y)
width= max_x-min_x + 1
height = max_y-min_y + 1
result = [['#' for _ in range(height)] for _ in range(width)]
for x,y in check:
    result[x-min_x][y-min_y] = '.'

for i in range(width):
    for j in range(height):
        print(result[i][j],end="")
    print()