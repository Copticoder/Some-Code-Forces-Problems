k=int(input())
months=list(map(int,input().split()))
months=sorted(months,reverse=True)
counter=0
while k>0 and counter < len(months):
    k-=months[counter]
    counter+=1
if k>0:
    print(-1)
else:
    print(counter)
