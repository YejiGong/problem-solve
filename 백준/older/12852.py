n=int(input())
case=0
lists=[float("inf") for i in range(n+1)]
lists[1]=0
steps=[[] for _ in range(n+1)]
steps[1]=[1]
for i in range(1,n):
    if i+1<=n and lists[i]+1<lists[i+1]:
        lists[i+1]=lists[i]+1
        steps[i+1]=steps[i]+[i]
    if 3*i<=n and lists[i]+1<lists[3*i]:
        lists[3*i]=lists[i]+1
        steps[3*i]=steps[i]+[i]
    if 2*i<=n and lists[i]+1<lists[2*i]:
        lists[2*i]=lists[i]+1
        steps[2*i]=steps[i]+[i]
print(lists[n])
steps[n]+=[n]
print(*sorted(list(set(steps[n])), reverse=True))
