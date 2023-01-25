import sys
input = sys.stdin.readline
N, B = map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(N)]

def mul(n,mtr1,mtr2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mtr1[i][k]*mtr2[k][j]
            result[i][j]%=1000
    return result

def div(n,b,mtr):
    if b==1:
        return mtr
    elif b==2:
        return mul(n,mtr,mtr)
    else:
        tmp = div(n,b//2,mtr)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),mtr)

ans=div(N,B,matrix)
for i in ans:
    for j in i:
        print(j%1000, end=' ')
    print()