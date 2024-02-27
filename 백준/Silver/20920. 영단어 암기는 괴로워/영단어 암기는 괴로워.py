import sys
input = sys.stdin.readline
N, M = map(int,input().split())
words={}
for _ in range(N):
    tmp = input().rstrip()
    if len(tmp)>=M:
        if tmp in words.keys():
            words[tmp]+=1
        else:
            words[tmp]=1
result = list(set(words.keys()))
result.sort(key=lambda x:(-words[x],-len(x),x))
for i in result:
    print(i)