n=int(input())
stones=list(input())
x=1
counter=0
while x<len(stones):
    if stones[x]==stones[x-1]:
        del stones[x-1]
        x=0
        counter+=1
    x+=1
print(counter)
