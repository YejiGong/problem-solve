n=int(input())
str_lists=[]
for i in range(n):
    k=str(input())
    str_lists.append(k)
str_lists=list(set(str_lists))
str_lists=sorted(str_lists)
str_lists=sorted(str_lists,key=len)
for i in str_lists:
    print(i)
