# 7 11
#7 13 
# 7 8 9 10 11 12 13

x,*y=input().split(' ')
x=int(x)
y=int(*y)
counter=0
i=2
j=x+1
while i<=j:
    if j%i==0:
        counter+=1
    i+=1
    if counter >1 and j<y:
        j+=1
        counter=0
        i=2
if counter in {0,1} and j == y:
    print('YES')
else:
    print('NO')