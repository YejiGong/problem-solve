N = int(input())
tops = list(map(int,input().split()))
result = [0 for _ in range(N)]
stack = [(tops[0],1)]
for i in range(1,N):
    while(len(stack)>0 and stack[-1][0]<tops[i]):
        stack.pop()
    result[i] = stack[-1][1] if len(stack)>0 else 0
    stack.append((tops[i], i+1))

print(*result)