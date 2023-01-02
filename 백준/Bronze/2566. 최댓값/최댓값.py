import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

max_value = max(map(max,arr))
indices = [(i,j) for i in range(9) for j in range(9) if arr[i][j]==max_value]

print(max_value)
print(indices[0][0]+1, indices[0][1]+1)