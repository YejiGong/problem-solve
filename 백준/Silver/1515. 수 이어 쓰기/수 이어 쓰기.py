import math
 
n = list(map(str,input().strip()))
 
i = 1
now_point = 0
while now_point <len(n) :
    temp = str(i)
 
    for j in range(len(temp)):
        if now_point >= len(n):
            break
        if temp[j] == n[now_point]:
            now_point+=1
    
    i+=1

print(i-1)