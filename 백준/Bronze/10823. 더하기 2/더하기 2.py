res = ''
while(True):
    try:
        res+=input()
    except:
        break
res = list(map(int,res.split(",")))
print(sum(res))