T=input()
S=input()
while len(S)!=len(T):
    if S[-1]=='A':
        S=S[:-1]
    elif S[-1]=='B':
        S=S[:-1]
        S=S[::-1]

if S==T:
    print(1)
else:
    print(0)