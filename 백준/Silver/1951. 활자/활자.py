n=int(input())
s = [0 for i in range(10)]
point = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            s[int(i)] += point
        n -= 1
    if n < 10:
        for i in range(n + 1):
            s[i] += point
        s[0] -= point
        break
    else:
        for i in range(10):
            s[i] += (n // 10 + 1) * point
    s[0] -= point
    point *= 10
    n //= 10

print(sum(s) % 1234567)