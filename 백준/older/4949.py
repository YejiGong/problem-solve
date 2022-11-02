while(True):
    string = input().rstrip()
    if string=='.':
        break
    stack=[]
    flag=True
    
    for tmp in string:
        if tmp=='(' or tmp=='[':
            stack.append(tmp)
        if tmp==')':
            if stack and stack[-1]=='(':
                stack.pop()
            elif (stack and stack[-1]!='(') or not stack :
                print('no')
                flag=False
                break
        if tmp==']':
            if stack and stack[-1]=='[':
                stack.pop()
            elif (stack and stack[-1]!='[') or not stack :
                print('no')
                flag=False
                break
    
    if flag and not stack:
        print('yes')
    elif flag and stack:
        print('no')
