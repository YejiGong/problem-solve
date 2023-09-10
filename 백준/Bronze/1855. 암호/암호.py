k=int(input())
tmp = input()
num=len(tmp)//k
arr = [[] for _ in range(k)]

for i in range(1,num+1):
    if i%2==1:
        for j in range(k):
            arr[j].append(tmp[j])
        tmp=tmp[k:]
    else:
        for j in range(k):
            arr[j].append(tmp[k-j-1])
        tmp=tmp[k:]
ans=''
for a in arr:
    for i in a:
        ans += i
print(ans)