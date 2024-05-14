T = int(input())
arr=[0 for _ in range(101)]
arr[4] = 2
arr[5] = 1
arr[6] = 0
for i in range(7,101):
    arr[i] = 1
for i in range(T):
    n = int(input())
    print(arr[n])