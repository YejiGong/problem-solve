tmp = input()
i=0
NOP = 0
while i<len(tmp):
    if tmp[i].isupper():
        #대문자 ->명령
        if i%4!=0:
            #NOP추가해야함
            tmp = tmp[:i]+" "+tmp[i:]
            NOP+=1
    i+=1

print(NOP)