n,*m=input().split()
n=int(n)
m=int(*m)
solCount=0
a=0
while a<=m and a*a <=n:
    b=n-a**2
    if a+b**2==m:
        solCount+=1
    a+=1
print(solCount)    