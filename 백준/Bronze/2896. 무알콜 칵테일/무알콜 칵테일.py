A,B,C = map(int,input().split())
I,J,K = map(int,input().split())
t = min(A/I, B/J, C/K)
print(A-I*t, B-J*t, C-K*t)