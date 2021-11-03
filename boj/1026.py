import sys
n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A_=[i for i in A]
B=list(map(int,sys.stdin.readline().split()))
B_=[0 for i in range(n)]
q=[i for i in A]
q.sort(reverse=True)
q_=[i for i in B]
q_.sort()
result=0
for i in range(n):
    B_[A.index(q[i])]=q_[i]
    A[A.index(q[i])]=-1
    
for i in range(n):
    result+=(A_[i]*B_[i])

print(result)
