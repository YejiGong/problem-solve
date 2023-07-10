import sys
input = sys.stdin.readline
N=int(input())
A,B=map(int,input().split())
data = set()
for _ in range(N):
    data.add(tuple(map(int,input().split())))

result = 0
for i in data:
    if (i[0]+A,i[1]) in data and (i[0],i[1]+B) in data and (i[0]+A, i[1]+B) in data:
        result+=1
print(result)