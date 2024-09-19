T=int(input())
tmp = 0
def dist(o1,o2):
    return abs(o2[0]-o1[0])**2+abs(o2[1]-o1[1])**2
for _ in range(T):
    square = []
    for _ in range(4):
        a, b = map(int, input().split())
        square.append([a, b])
    square = sorted(square)
    
    for x,y in square:
        if x==0 and y==0:
            tmp+=1
    
    if tmp==4:
        print(0)
        tmp = 0
    elif (dist(square[0], square[1]) == dist(square[0], square[2]) == dist(square[1], square[3])
        and dist(square[1],square[2])==dist(square[0],square[3])):
        print(1)
    else:
        print(0)