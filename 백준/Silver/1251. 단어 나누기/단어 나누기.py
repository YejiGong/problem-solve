s = input()
dict = []
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        tmp = s[:i][::-1]+s[i:j][::-1]+s[j:][::-1]
        dict.append(tmp)

dict.sort()
print(dict[0])