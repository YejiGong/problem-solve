N = int(input())
lifeguards = [0]*1000
work = []
for _ in range(N):
    start, end = map(int, input().split())
    work.append((start, end))
    for i in range(start, end):
        lifeguards[i] += 1

ans = 0
for w in work:
    start, end = w[0], w[1]
    for i in range(start, end):
        lifeguards[i] -= 1
    time = 0    
    for lifeguard in lifeguards:
        if lifeguard > 0:        
            time += 1
    ans = max(time, ans)  
    for i in range(start, end):
        lifeguards[i] += 1  
        
print(ans)