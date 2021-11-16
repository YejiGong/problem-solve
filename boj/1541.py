n=input().split('-')
cal=[]
for i in n:
    tmp=i.split('+')
    tmp=[int(j)*(-1) for j in tmp]
    cal.append(sum(tmp))

cal[0]=cal[0]*(-1)
print(sum(cal))
