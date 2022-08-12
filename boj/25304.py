x=int(input())
n=int(input())
sum_products=0
for i in range(n):
    a,b = map(int,input().split())
    sum_products+=(a*b)
if(x==sum_products):
    print("Yes")
else:
    print("No")
