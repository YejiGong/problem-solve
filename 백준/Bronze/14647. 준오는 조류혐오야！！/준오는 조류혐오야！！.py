n,m=map(int,input().split())
bingo = []
row, col = [], []
for _ in range(n):
    tmp = list(map(str,input().split()))
    bingo.append(tmp)
    rowCnt = 0
    for i in tmp:
        rowCnt+=i.count('9')
    row.append(rowCnt)
for i in range(m):
    colCnt = 0
    for j in range(n):
        colCnt += bingo[j][i].count('9')
    col.append(colCnt)
print(sum(row)-max(max(row),max(col)))