while True:
    tmp = input()
    if(tmp=='#'):
        break
    else:
        res = 0
        for i in tmp:
            if(i.isalpha()==True and i.lower() in ['a','e','i','o','u']):
                res +=1
        print(res)