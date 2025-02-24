N = int(input())
arr = list(set([input() for _ in range(N)]))
N = len(arr)
arr.sort()
res = []
num = 1
pattern = arr[0]
for i in range(1,N):
    if arr[i][:len(arr[i-1])] == arr[i-1]:
        num += 1
    else:
        res.append(num)
        num = 1
res.append(num)
print(len(res))