n=int(input())
for i in range(2*n):
    print(' ',end='')
print(0)
for j in range(1,n+1):
    for x in range(((2*n)-(2*j))):
        print(' ',end='')
    for z in range(0,j+1):
        print(z,end=' ')
    for l in range(j-1,-1,-1):
        if l==0:
            print(l,end='')
        else:
            print(l,end=' ')
    print('')
e=2
for m in range(n-1,0,-1):
    for c in range(e):
        print(' ',end='')
    e+=2
    for p in range(0,m+1):
        print(p,end=' ')
    for o in range(m-1,-1,-1):
        if o==0:
            print(o,end='')
        else:
            print(o,end=' ')
    print('')
for q in range(2*n):
    print(' ',end='')
print(0)

