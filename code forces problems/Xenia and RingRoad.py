n,*m=input().split(' ')
n=int(n)
m=int(*m)
tasks=list(map(int, input().split()))
temp=1
counter=0
steps=0
while m:
    if tasks[counter]<temp:
        temp=n-temp
        steps+=temp+tasks[counter]
      
    else:
        steps+=tasks[counter]-temp
    temp=tasks[counter]
    counter+=1
    m-=1
print(steps)