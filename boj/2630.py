N=int(input())
paper=[]
result_white=0
result_blue=0

for _ in range(N):
    paper.append(list(map(int,input().split())))

def check(org_x,org_y,n):
    global result_white, result_blue
    color = paper[org_x][org_y]
    for i in range(org_x, org_x+n):
        for j in range(org_y,org_y+n):
            if color != paper[i][j]:
                check(org_x,org_y,n//2)
                check(org_x,org_y+n//2,n//2)
                check(org_x+n//2,org_y,n//2)
                check(org_x+n//2,org_y+n//2,n//2)
                return
    if color == 0:
        result_white+=1
    else:
        result_blue+=1

check(0,0,N)
print(result_white)
print(result_blue)
