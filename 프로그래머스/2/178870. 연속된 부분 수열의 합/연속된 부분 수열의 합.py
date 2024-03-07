def isNewStartIdxFinishIdx(start,finish):
    global startIdx
    global finishIdx
    global sequenceLength
    tmpLength = finish - start
    if(tmpLength<sequenceLength):
        startIdx = start
        finishIdx = finish
        sequenceLength = tmpLength
    elif (tmpLength==sequenceLength and start<startIdx):
        startIdx = start
        finishIdx = finish
    else:
        pass

def solution(sequence, k):
    global startIdx
    global finishIdx
    global sequenceLength
    startIdx= len(sequence)
    finishIdx = 0
    sequenceLength = len(sequence)
    arr = [0 for _ in range(len(sequence))]
    arr[0] = sequence[0]
    if(arr[0] == k):
        isNewStartIdxFinishIdx(0,0)
    for i in range(1,len(sequence)):
        arr[i] = arr[i-1]+sequence[i] #누적합
        if(sequence[i]==k):
            isNewStartIdxFinishIdx(i,i)
        elif(arr[i]==k):
            isNewStartIdxFinishIdx(0,i)
    #[1,2,3,4,5] -> [1,3,6,10,15]
    start, finish = 0,1
    while finish<len(sequence) and start<=finish:
        tmp = arr[finish] - arr[start]
        if(tmp==k):
            isNewStartIdxFinishIdx(start+1,finish)
            start+=1
            finish+=1
        elif(tmp<k):
            finish+=1
        else:
            start+=1
    return [startIdx, finishIdx]