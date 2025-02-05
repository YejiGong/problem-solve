arr = list(map(str,input()))
stack=[]
cnt = 0
res = 0
for i in range(len(arr)):
    if arr[i] == '(':
        cnt += 1 #막대기의 개수를 계산
        stack.append(i)
    else:
        cnt-=1
        idx = stack.pop()
        if i-idx==1: #레이저
            res+=cnt
        else:
            res+=1
print(res)