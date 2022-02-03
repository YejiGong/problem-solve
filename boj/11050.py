n,k=map(int,input().split())

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

first=factorial(n)
second=factorial(n-k)
third=factorial(k)

result=first//(second*third)
print(result)
