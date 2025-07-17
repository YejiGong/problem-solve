str = [int(i) for i in input()]
N = len(str)//2
offset = 0
while N>0:
    flag = False
    for i in range(0, len(str)-2*N+1):
        left_sum = sum(str[i:i+N])
        right_sum = sum(str[i+N:i+2*N])
        if left_sum == right_sum:
            flag = True
            break
    if(flag):
        break
    else:
        N-=1

print(N*2)