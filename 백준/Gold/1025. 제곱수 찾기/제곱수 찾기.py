import math
n,m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(map(str,input().strip())))

res = -1
for i in range(n):
    for j in range(m):
        for a in range(-n, n):
            for b in range(-m,m):
                num = ''
                y,x = i,j
                while 0<=y<n and 0<=x<m:
                    num += table[y][x]
                    if a==0 and b==0:
                        break
                    if int(math.sqrt(int(num)))**2 == int(num) :
                        res = max(int(num), res)
                    y+=a
                    x+=b
print(res)
            