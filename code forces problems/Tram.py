n=int(input())
tram=[0]
maxmum=0
while n:
    outer,*pas=input().split(' ')
    if outer==0:
        tram[0]+=int(*pas)
    else:
        tram[0]-=int(outer)
        tram[0]+=int(*pas)
        maxmum = max(maxmum, tram[0])
    n-=1
print(maxmum)