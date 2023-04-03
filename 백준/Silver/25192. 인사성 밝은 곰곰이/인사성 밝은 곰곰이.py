N= int(input())
members={}
result = 0
for _ in range(N):
    tmp = input()
    if tmp=="ENTER":
        for key,value in members.items():
            if value==1:
                result+=1
        members={}
    else:
        if tmp not in members:
            members[tmp]=1

for key,value in members.items():
    if value==1:
        result+=1

print(result)