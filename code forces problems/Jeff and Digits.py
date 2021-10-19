n=int(input())
digits=list(map(int,input().split()))
digits=sorted(digits,reverse=True)
fives = []
if 0 in digits:
    
    lastFive=digits.index(0)
    fives=digits[0:lastFive]
    digits=digits[lastFive:]
    if len(fives) <9:
        print(0)
    else:
        while (len(fives)*5)%9!=0:
            fives.pop(0)
        for x in digits:
            fives.append(x)
        for j in fives:
            print(j,end='')
else:   
    print(-1)