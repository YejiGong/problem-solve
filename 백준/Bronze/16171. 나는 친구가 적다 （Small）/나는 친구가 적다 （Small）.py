S=input()
K=input()
tmp = ''
for i in S:
    if i.isalpha():
        tmp+=i
if K in tmp:
    print(1)
else:
    print(0)