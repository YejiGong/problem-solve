import math
def solution(r1, r2):
    answer = 0
    for x in range(0,r2+1):
        tmp = (int)(abs(r2**2 - x**2)**0.5) #tmp^2+x^2=r2^2인 tmp
        if(tmp<x): #(x,0) ~ (x,tmp) 까지 원 안에 속함 - 축에 있는 점 제외하고 계산
            answer += tmp*2
        else: #(x,0) ~ (x,x) 까지 속함 - 축에 있는 점 제외하고 계산
            answer += x*2 -1 
    print(answer)
    for x in range(0,r1):
        tmp = (abs(r1**2 - x**2)**0.5) #tmp^2+x^2=r2^2인 tmp
        if(tmp==int(tmp)):
            tmp = int(tmp) - 1
        else:
            tmp = int(tmp)
        if(tmp<x): #(x,0) ~ (x,tmp)까지 원 안에 속함 - 축에 있는 점 제외하고 계산
            answer -= tmp*2
        else: #(x,0) ~ (x,x)까지 원 안에 속함 - 축에 있는 점 제외하고 계산
            answer -= x*2 -1
    return answer*4 + (r2-r1+1)*4