n = int(input())
p=1000000007

def mul(A,B):
    m = len(A)
    result = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            tmp = 0
            for k in range(m):
                tmp += A[i][k]*B[k][j]
            result[i][j] = tmp%p

    return result

def square(A,k):
    if k == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= p
        return A

    tmp = square(A,k//2)
    if k%2:
        return mul(mul(tmp,tmp), A)
    else:
        return mul(tmp,tmp)

fib = [[1,1], [1,0]]
print(square(fib,n)[0][1])