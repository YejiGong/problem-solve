board = input().split(".")
result = []
flag = True
for i in board:
  if len(i)%4 == 1 or len(i)%4==3:
    flag = False
    break
  else:
    if len(i)==2:
        result.append('BB')
    else:
        Anum = len(i)//4
        Bnum = (len(i)%4)//2
        tmp = 'AAAA'*Anum + 'BB'*Bnum
        result.append(tmp)
if(flag==False):
    print("-1")
else:
  for i in range(len(result)):
    if (i != len(result)-1):
        print(result[i], end='.')
    else:
        print(result[i])

    