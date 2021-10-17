n,*candy=input().split(' ')
candy=int(*candy)
n=int(n)
childCandy=list(map(int,input().split()))
indexList=[x+1 for x in range(len(childCandy))]
while len(indexList)!=1:
    if childCandy[0] - candy > 0:
        childCandy.append(childCandy[0]-candy)
        indexList.append(indexList[0])
    childCandy.pop(0)
    indexList.pop(0)
print(indexList[0])