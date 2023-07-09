name = [i for i in input()]
alphabet = [0 for _ in range(26)]
odd = 0
even = 0
for i in name:
    num = ord(i) - 65
    alphabet[num]+=1
for i in alphabet:
    if i != 0 :
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

result = ''
if (len(name)%2==0 and odd == 0) or (len(name)%2==1 and odd <= 1):
    for i in range(26):
        if alphabet[i] != 0:
            tmp = chr(i+65)*alphabet[i]
            lenth = len(result)
            if lenth == 0:
                result = tmp
            elif lenth%2==0:
                result = result[:lenth//2]+tmp+result[lenth//2:]
            else:
                tmp_lenth = len(tmp)
                result = result[:lenth//2]+tmp[:tmp_lenth//2]+result[lenth//2]+tmp[tmp_lenth//2:]+result[lenth//2+1:]
    print(result)
else:
    print("I'm Sorry Hansoo")