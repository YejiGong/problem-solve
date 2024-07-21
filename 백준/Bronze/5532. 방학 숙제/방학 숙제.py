import math
L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

mathD = math.ceil(B/D)
koreanD = math.ceil(A/C)
print(L - max(mathD, koreanD))
