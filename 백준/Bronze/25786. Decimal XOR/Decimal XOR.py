a = input()
b = input()
if(len(a)!=len(b)):
    if(len(a)>len(b)):
        diff = len(a) - len(b)
        b = '0'*diff + b
    else:
        diff = len(b) - len(a)
        a = '0'*diff + a
result = ''
for i in range(len(a)):
    if((int(a[i])<=2 and int(b[i])<=2) or (int(a[i])>=7 and int(b[i])>=7)):
        result += '0'
    else:
        result += '9'
print(result)