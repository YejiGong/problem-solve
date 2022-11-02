n, m =map(int,input().split())
a_elem = set(list(map(int,input().split())))
b_elem= set(list(map(int,input().split())))
result=a_elem^b_elem
print(len(result))
