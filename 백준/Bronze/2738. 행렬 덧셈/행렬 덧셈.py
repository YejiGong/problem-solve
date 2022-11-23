import sys
input=sys.stdin.readline
n,m = map(int,input().split())
matrix_a = []
matrix_b = []
matrix_result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    matrix_a.append(tmp)

for i in range(n):
    tmp = list(map(int,input().split()))
    matrix_b.append(tmp)

for i in range(n):
    for j in range(m):
        matrix_result[i][j] = matrix_a[i][j]+matrix_b[i][j]

for i in range(n):
    for j in range(m):
        print(matrix_result[i][j], end=' ')
    print('')