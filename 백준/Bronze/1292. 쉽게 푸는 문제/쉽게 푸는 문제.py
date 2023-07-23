a, b = map(int,input().split())
tmp = [0 for _ in range(b+1)]
num = 1
idx = 0
cnt = 0
while True:
    if idx>b:
        break
    if cnt==num:
        num+=1
        cnt=0
        continue
    tmp[idx] = num
    idx+=1
    cnt+=1

print(sum(tmp[a-1:b]))