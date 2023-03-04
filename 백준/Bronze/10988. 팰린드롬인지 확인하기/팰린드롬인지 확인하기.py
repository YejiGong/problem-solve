keyword = input()
check=True
for i in range(len(keyword)//2):
    if keyword[i]==keyword[len(keyword)-i-1]:
        pass
    else:
        check=False
        break
if check:
    print(1)
else:
    print(0)