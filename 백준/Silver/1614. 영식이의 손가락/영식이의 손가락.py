n = int(input())
m = int(input())

if m == 0:
    print(n-1)

else:
    if n == 1:
        print(m*8)
    elif n == 2:
        if m % 2 == 0: 
            print((m*4)+1)
        else:
            print((m*4)+3)
    elif n == 3:
        print((m*4)+2)
    elif n == 4:
        if m % 2 == 0:
            print((m*4)+3)
        else:
            print((m*4)+1)
    else:
        print((m*8)+4)