s_str = str(input())
s = list(s_str)


k = ['K','O','R','E','A']
y = ['Y','O','N','S','E','I']

for v in s:
    if v == k[0]:
        k.remove(v)
        if len(k) == 0:
            print("KOREA")
            break
    if v == y[0]:
        y.remove(v)
        if len(y) == 0:
            print("YONSEI")
            break