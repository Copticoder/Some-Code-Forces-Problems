n=int(input())
coder=list(map(int,input().split(' ')))
minmum=coder[0]
maxmum=coder[0]
counter=0
for i in coder:
    if i <minmum:
        counter+=1
        minmum=i
    elif i > maxmum:
        counter+=1
        maxmum=i
print(counter)
