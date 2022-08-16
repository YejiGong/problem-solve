import fractions
n=int(input())
rings=list(map(int,input().split()))
base=rings[0]
for i in rings[1:]:
    k = fractions.Fraction(base,i)
    print(str(k.numerator)+"/"+str(k.denominator))
