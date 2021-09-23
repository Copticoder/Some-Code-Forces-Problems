n=int(input())
counter=0
while n:
    probList=list(map(int,input().split()))
    if sum(probList)>=2:
        counter+=1
    n-=1
print(counter)