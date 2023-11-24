def makeBinaryNumber(number):
    reverseBinaryNumber = []
    while number != 1:
        reverseBinaryNumber.append(str(number % 2))
        number //= 2
    reverseBinaryNumber.append("1")
    binaryNumber = ''.join(reverseBinaryNumber[::-1])
    binaryTreeSize = 1
    while binaryTreeSize < len(binaryNumber):
        binaryTreeSize = (binaryTreeSize + 1) * 2 - 1
    binaryNumber = "0" * (binaryTreeSize - len(binaryNumber)) + binaryNumber
    return binaryNumber

def check(start, end, arr):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    left = check(start, mid - 1, arr)
    if not left or (arr[mid] == "0" and left == "1"):
        return False
    right = check(mid + 1, end, arr)
    if not right or (arr[mid] == "0" and right == "1"):
        return False
    if arr[mid]=="0" and left=="0" and right == "0":
        return "0"
    else:
        return "1"


def solution(numbers):
    n = len(numbers)
    answer=[]
    for number in numbers:
        tmpTree = makeBinaryNumber(number) #이진수로 표현
        if check(0,len(tmpTree)-1, tmpTree):
            answer.append(1)
        else:
            answer.append(0)
    return answer