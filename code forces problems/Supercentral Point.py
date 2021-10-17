n=int(input())
counter =n
coord=[]
sol=0
while counter:
    x,*y=input().split(' ')
    coord.append([int(x),int(*y)])
    counter-=1
for j in range(n):
    r,l,u,d=False,False,False,False
    for i in range(n):
        if coord[j][0]>coord[i][0] and coord[j][1] == coord[i][1]:
            l=True
        if coord[j][0]<coord[i][0] and coord[j][1] == coord[i][1]:
            r=True
        if coord[j][1]>coord[i][1] and coord[j][0] == coord[i][0]:
            d=True 
        if coord[j][1]<coord[i][1] and coord[j][0] == coord[i][0]:
            u=True
    if l and d and r and u:
       sol+=1 
print(sol)