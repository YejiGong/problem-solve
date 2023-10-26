S=list(map(str,input()))
counter = dict()
for s in S:
    if s in counter:
        counter[s] +=1
    else:
        counter[s] = 1
def dfs(pre, cnt):
    if cnt == len(S):
        return 1
    ans = 0
    for key in counter.keys():
        if pre == key:
            continue
        if counter[key]==0:
            continue
        counter[key]-=1
        ans += dfs(key,cnt+1)
        counter[key]+=1
    return ans
ans = dfs('',0)
print(ans)