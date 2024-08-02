N, J, H = map(int,input().split())
result = 1
cur_N = N
while True:
    split_num = [i for i in range(1,cur_N+1, 2)]
    if (J-H == 1 and H in split_num) or (H-J==1 and J in split_num):
        print(result)
        break
    else:
        cur_N //= 2
        J = (J+1)//2
        H = (H+1)//2
        result += 1

