import sys
input = sys.stdin.readline

N=0
dictionary = {}
while True:
    word = input().rstrip()
    if word!='':
        N+=1
        if word in dictionary.keys():
            dictionary[word]+=1
        else:
            dictionary[word]=1
    else:
        break

for i in sorted(list(dictionary.keys())):
    tmp = (dictionary[i]/N)*100
    print("%s %.4f" %(i,tmp))