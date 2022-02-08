n=int(input())
m=int(input())
k=int(str(n)[:-2]+'00')//m
while(True):
    if str(k*m)[:-2]==str(n)[:-2]:
        print(str(k*m)[-2:])
        break
    else:
        k+=1
