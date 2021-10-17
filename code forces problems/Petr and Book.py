n=int(input())
readDays=list(map(int,input().split()))
i=0
while n>0:
    n -= readDays[i]
    i+=1
    if i > 6 and n>0:
        i=0
print(i)
    