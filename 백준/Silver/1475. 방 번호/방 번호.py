N=input()
numbers=[0 for _ in range(10)]
for i in N:
    if(i=='9' and numbers[9]>numbers[6]):
        i ='6'
    elif(i=='6' and numbers[6]>numbers[9]):
        i = '9'
    numbers[int(i)]+=1

print(max(numbers))