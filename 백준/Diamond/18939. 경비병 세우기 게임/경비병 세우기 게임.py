T= int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    if(max(N,M)<2*K):
        print('Yuto')
    else:
        min_num = N*M
        if(min_num%2==1):
            print('Yuto')
        else:
            print('Platina')