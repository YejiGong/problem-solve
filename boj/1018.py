n,m=map(int,input().split())
chess=[]
for _ in range(n):
    tmp=list(str(input()))
    chess.append(tmp)

num=float('inf')

checking_w='WBWBWBWB'
checking_b='BWBWBWBW'
def check(x,y):
    check_w=0
    check_b=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if chess[y+i][x+j]!='W':
                    check_w+=1
                if chess[y+i][x+j]!='B':
                    check_b+=1
            else:
                if chess[y+i][x+j]!='B':
                    check_w+=1
                if chess[y+i][x+j]!='W':
                    check_b+=1
    return min(check_w, check_b)

for i in range(n-7):
    for j in range(m-7):
        tmp=check(j,i)
        if tmp<num:
            num=tmp
        if num==0:
            break
    if num==0:
        break

print(num)
