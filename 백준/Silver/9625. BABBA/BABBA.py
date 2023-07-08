K=int(input())
A=1
B=0
for i in range(K):
    tmp_b = A+B
    tmp_a = B
    B = tmp_b
    A = tmp_a

print(A, B)
