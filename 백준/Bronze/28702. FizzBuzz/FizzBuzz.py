a1 = input()
a2 = input()
a3 = input()
ans = 0
if(a1 != 'FizzBuzz' and a1 != 'Fizz' and a1 != 'Buzz'):
    ans = int(a1) + 3
if(a2 != 'FizzBuzz' and a2 != 'Fizz' and a2 != 'Buzz'):
    ans = int(a2) + 2
if(a3 != 'FizzBuzz' and a3 != 'Fizz' and a3 != 'Buzz'):
    ans = int(a3) + 1
if ans%3 == 0 and ans%5 == 0:
    print('FizzBuzz')
elif ans%3 == 0:
    print('Fizz')
elif ans%5 == 0:
    print('Buzz')
else:
    print(ans)