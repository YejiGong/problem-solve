n = int(input())
x = list(map(int,input().split()))
sum_x = [0 for _ in range(n)]
result = 0
sum_x[0] = x[0]
for i in range(1,len(x)):
    sum_x[i] = sum_x[i-1]+x[i]
for i in range(len(x)):
    result += (sum_x[-1]-sum_x[i])*x[i]
print(result)