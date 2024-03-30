N=int(input())
members=[0 for _ in range(N+1)]
vote=list(map(int,input().split()))
max_val = 0
max_idx = -1
for i in vote:
    members[i]+=1
    if(members[i]>max_val and i!=0):
        max_val = members[i]
        max_idx = i
    elif(members[i]==max_val and i!=max_idx and i!=0):
        max_idx=-1

if(max_idx==-1):
    print("skipped")
else:
    print(max_idx)
