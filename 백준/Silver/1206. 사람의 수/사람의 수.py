import math
N= int(input())
data = list((input() for _ in range(N)))
#num*people<=10*N
#people<=10*N/num
avg = [0] * N

for i in range(N):
    # Convert to float, get fractional part, and round to 3 decimal places
    value = float(data[i])
    avg[i] = round(value - math.floor(value), 3)

cases = [0] * 1001
for num in range(1, 1001):
    for score in range(1, num + 1):
        cases[score] = math.floor((score / num) * 1000) / 1000.0

    flag = True
    for j in range(N):
        if avg[j] not in cases[:num + 1]:
            flag = False
            break

    if flag:
        print(num)
        break