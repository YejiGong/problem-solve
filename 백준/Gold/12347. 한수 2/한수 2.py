N=int(input())
#ex)한자리수: 모두 포함, 두자리수: 모두 포함 -> 99개,
# 세자리수:111,123, 135, 147,159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 368, 420, 432, 444, 456, 468, ... -> 100자리수마다 5개
# 네자리수:1111, 1234, 1357, 2222, 2345, 2468, 3210, 3333, 3456, 3579, 4321, 4444, 4567, 5432, 5555, 5678, 6420, 6543, 6666, 6789 -> ?
# N은 abc인 3자리 수라고 하자, ab를 기준으로 그 뒤에 올 수 있는 c의 후보자를 구하고 거기서부터 밑으로 내려오자.
def getDiff(N):
    return int(str(N)[1])-int(str(N)[0])

def getDiffResult(firstNum, numDigits, diff):
    res = str(firstNum)
    lastNum = firstNum
    for i in range(1,numDigits):
        lastNum += diff
        res += str(lastNum)
    return int(res)

strNum = str(N)
numLength = len(str(N))
if numLength<=2:
    print(N)
else:
    result = 99 #2자리수까지 모두 포함
    for i in range(3,numLength+1):
        #자리수별로 계산하기
        for j in range(1,10):
            #첫번째 자릿수가 j일때의 경우의 수 구하기
            #0<=j+diff*(i-1)<10이면 등차수열인 숫자를 만들 수 있다.
            #만약 j가 1일때, diff의 범위는 0~4이므로 총 5개를 만들 수 있음.
            #j가 2일때 diff의 범위는 -1~3이므로 총 5개를 만들 수 있다.
            #즉, -j//(i-1)<=diff<(10-j)//(i-1)
            if i<numLength or (i==numLength and j<int(strNum[0])):
                #아직 마지막 자릿수 아니거나, 마지막 자릿수지만 N의 첫번째 자릿수보다 작은 경우에 대해 계산 중
                num = (9 - j) // (i - 1) + j // (i - 1) + 1
                result+=num
            else:
                #ex) N=5421인데 i==4, j==5인 경우. N보다 작은 경우에 대해서만 계산해야함.
                minDiff = (j//(i-1))*(-1)
                maxDiff = (9-j)//(i-1)
                result += sum(1 for k in range(minDiff, maxDiff+1) if getDiffResult(int(strNum[0]), i, k) <= N)
                break
    print(result)