import sys
input = sys.stdin.readline
N=int(input())
arr=[]
result = 0
#2 4 1 2 2 5 1
#[0,1] [1,2] [1,3] [2,3] [1,4] [3,4] [3,5] [4,5] [1,5] [5,6] (idx)
#[2,4] [4,1] [4,2] [4,2] [4,5] [1,2] [2,2] [2,5] [2,5] [5,1] (val)
dp = [0 for _ in range(N)]
for i in range(N):
    tmp = int(input())
    tmp_q = 1
    if(i==0):
        arr.append((tmp,1))
        continue
    else:
        left = len(arr) - 1
        while arr and left>=0:
            if(arr[left][0]<tmp):
                t, q = arr.pop()
                result += q
                tmp_q = 1
            elif(arr[left][0]==tmp):
                t,q = arr.pop()
                result += q
                tmp_q+=q
            else:
                result += 1
                break
            left -= 1
    arr.append((tmp, tmp_q))
print(result)
