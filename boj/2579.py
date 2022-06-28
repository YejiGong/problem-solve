num=int(input())
steps=[]
for _ in range(num):
    steps.append(int(input()))
value=[0 for _ in range(num)]
value[0]=steps[0]
if(num>1):
    value[1]=max(value[0]+steps[1], steps[1])
if(num>2):
    value[2]=max(steps[1]+steps[2], value[0]+steps[2])
for i in range(3,num):
    value[i]=max(value[i-2]+steps[i], value[i-3]+steps[i-1]+steps[i])

print(value[num-1])
