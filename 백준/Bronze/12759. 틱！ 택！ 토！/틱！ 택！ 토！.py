playerFirst = int(input())
playerSecond = 1 if playerFirst==2 else 2
graph=[[0 for _ in range(4)] for _ in range(4)]
flag = False
def checkIfFinish(x,y, player):
    global flag
    column = set(graph[i][j] for i,j in [(x,1), (x,2), (x,3)])
    row = set(graph[i][j] for i,j in [(1,y), (2,y), (3,y)])
    diagonalLeft = set(graph[i][j] for i,j in [(1,1),(2,2),(3,3)])
    diagonalRight = set(graph[i][j] for i,j in [(1,3),(2,2),(3,1)])

    if len(column)==1 or len(row)==1:
        flag=True
        print(player)
    elif (x,y) in [(1,1),(2,2),(3,3)] and len(diagonalLeft)==1:
        flag=True
        print(player)
    elif (x,y) in [(1,3),(2,2),(3,1)] and len(diagonalRight)==1:
        flag=True
        print(player)

for i in range(9):
    x, y= map(int,input().split())
    graph[x][y] = playerFirst if i%2==0 else playerSecond
    if(flag==False):
        checkIfFinish(x,y,graph[x][y])

if(flag==False):
    print(0)