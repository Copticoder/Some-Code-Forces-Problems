n,*m=input().split()
n=int(n)
m=int(*m)
tvs=list(map(int,input().split()))
tvs=sorted(tvs)
sumSale=0
i=0
counter=0
while i< len(tvs) and tvs[i] <0 and counter<m:
    sumSale+=abs(tvs[i])
    i+=1
    counter+=1
print(sumSale)