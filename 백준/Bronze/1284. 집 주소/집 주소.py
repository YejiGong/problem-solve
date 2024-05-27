while True:
    tmp = input()
    if(tmp=='0'):
        break
    else:
        middle = len(tmp) - 1
        nums = 0
        for i in tmp:
            if i=='0':
                nums+=4
            elif i=='1':
                nums+=2
            else:
                nums+=3
        print(middle+nums+2)