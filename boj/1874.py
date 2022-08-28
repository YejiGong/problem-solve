import sys
input=sys.stdin.readline
n=int(input())
nums=[]
result_set=[]
count=1
temp=True
for _ in range(n):
    cnt=int(input())
    while count<=cnt:
        nums.append(count)
        result_set.append('+')
        count+=1
    if nums[-1]==cnt:
        nums.pop()
        result_set.append('-')
    else:
        temp=False
if temp:
    for i in result_set:
        print(i)
else:
    print('NO')
