import sys
input = sys.stdin.readline
K,L = map(int,input().split())
student_set={}
#1<=L<=500,000, 0<=K<=100,000에 1초 : O(N)
for i in range(L):
    std = input()
    if(std in student_set.keys()):
        student_set.pop(std)
    student_set[std] = i
check = 0
arr = list(student_set.items())
for i in range(min(K, len(arr))):
    print(arr[i][0].rstrip())


