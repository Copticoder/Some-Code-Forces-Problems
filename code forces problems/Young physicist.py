forcNum=int(input())
listFrcs=[]
while forcNum:
    frcs=list(map(int,input().split(' ')))
    listFrcs.append(frcs)
    forcNum-=1
summer=0
for j in range(3):
    for i in range(len(listFrcs)):
        summer= listFrcs[i][j]+summer
    if summer != 0:
        print('NO')
        break
    else:
        continue
if summer == 0:
    print('YES')