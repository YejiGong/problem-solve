n=int(input())
fib = [0 for _ in range(n+1)]
if n>=1:
    fib[1] = 1
if n>=2:
    for i in range(2,n+1):
        fib[i] = fib[i-2] + fib[i-1]

print(fib[n])