a, b= map(int,input().split())
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
if b>10000000 : b=10000000

palindrome = [n for n in range(a,b+1) if str(n) == str(n)[::-1]]
for n in palindrome:
    if isPrime(n):
        print(n)
print(-1)