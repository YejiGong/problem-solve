import sys

inpyt = sys.stdin.readline

n,k=map(int,input().split())
a = list(map(int,input().split()))
ans = []

def merge_sort(arr):
    if len(arr) ==1:
        return arr

    mid = (len(arr) + 1)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    i,j=0,0
    new_arr=[]

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            new_arr.append(left_arr[i])
            ans.append(left_arr[i])
            i+=1
        else:
            new_arr.append(right_arr[j])
            ans.append(right_arr[j])
            j+=1
    while i<len(left_arr):
        new_arr.append(left_arr[i])
        ans.append(left_arr[i])
        i+=1
    while j<len(right_arr):
        new_arr.append(right_arr[j])
        ans.append(right_arr[j])
        j+=1

    return new_arr


merge_sort(a)

if len(ans)>=k:
    print(ans[k-1])
else:
    print(-1)