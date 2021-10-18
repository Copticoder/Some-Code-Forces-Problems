n,*k=input().split()
n=int(n)
k=int(*k)
if n%2 ==0:
    if k<=n//2:
        n-=1
        print(n-(2*(((n+1)//2) - k)))

    else:
        k-=n//2
        print(n-(2*((n//2) - k)))
elif k<=(n//2 +1):

    print(n-(2*((n//2 +1)-k)))
else:
    n-=1 
    k-=(n//2 +1)
    print(n-(2*((n+1)//2 -k)))
