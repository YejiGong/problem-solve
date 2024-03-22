import sys
input = sys.stdin.readline
K,L = map(int,input().split())
arr = []
student_set={}
#1<=L<=500,000, 0<=K<=100,000에 1초 : O(N)
for i in range(L):
    std = input().rstrip()
    student_set[std] = i
    arr.append(std)
check = 0
for i in range(L):
    if(student_set[arr[i]]==i):
        check += 1
        print(arr[i])
    if(check==K):
        break


