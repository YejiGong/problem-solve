k = float(input())

p = 1
q = 1

while(abs(p/q - k) > 10**-6):
    if p/q > k:
        q += 1
    else:
        p += 1
print("YES")
print(p, q)