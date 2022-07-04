n, m=map(int,input().split())
not_hear=set()
not_look=set()
for _ in range(n):
    not_hear.add(input())
for _ in range(m):
    not_look.add(input())
    
mix=sorted(list(not_hear&not_look))
print(len(mix))
for i in mix:
    print(i)
