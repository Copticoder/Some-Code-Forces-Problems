n,a,b=map(int,input().split())
line=[x for x in range(1,n+1)]
count=0
for i in line:
    if i-1>=a and n-i<=b:
        count+=1
print(count)
