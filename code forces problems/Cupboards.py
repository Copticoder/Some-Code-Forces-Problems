n=int(input())
lCup=[]
rCup=[]
open=0
closed=0
left=0
right=0
while n:
    l,*r=input().split(' ')
    lCup.append(int(l))
    rCup.append(int(*r))
    n-=1
for i in lCup:
    if i==0:
        closed+=1
    else:
        open+=1
left = min(closed, open)
closed=0
open=0
for x in rCup:
    if x==0:
        closed+=1
    else:
        open+=1
right = min(closed, open)
print(left+right)
