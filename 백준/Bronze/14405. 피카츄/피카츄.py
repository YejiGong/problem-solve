s = input()
start = 0
while start<len(s):
    if s[start:start+2]=='pi':
        start+=2
        continue
    elif s[start:start+2]=='ka':
        start+=2
        continue
    elif s[start:start+3]=='chu':
        start+=3
        continue
    else:
        break
if start!=len(s):
    print("NO")
else:
    print("YES")