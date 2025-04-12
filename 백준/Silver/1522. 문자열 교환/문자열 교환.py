str = input()
if(len(str)<=2):
    print(0)
else:
    a = str.count('a')
    min_val = 1e9
    str += str[0:a-1]
    for i in range(len(str) - (a-1)):
        min_val = min(min_val, str[i:i+a].count('b'))
    print(min_val)