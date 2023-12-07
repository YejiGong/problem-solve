phone_1=input()
phone_2=input()
res=''
for i in range(8):
    res+=phone_1[i]
    res+=phone_2[i]
while len(res)>2:
    tmp_res=''
    for i in range(0,len(res)-1):
        tmp=str((int(res[i])+int(res[i+1])))
        if len(tmp)>1:
            tmp_res+=tmp[-1]
        else:
            tmp_res+=tmp
    res=tmp_res
print(res)