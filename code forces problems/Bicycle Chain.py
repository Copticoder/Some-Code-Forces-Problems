n=int(input())
pedAxle=list(map(int,input().split()))
m=int(input())
reAxle=list(map(int,input().split()))
ratios=[]
for i in range(len(reAxle)):
    for j in range(len(pedAxle)):
        if reAxle[i]%pedAxle[j]==0:
            ratios.append(reAxle[i]/pedAxle[j])
ratios=sorted(ratios,reverse=True)
i=0
while i< len(ratios) and ratios[i] ==ratios[0]:
    i+=1
print(i)