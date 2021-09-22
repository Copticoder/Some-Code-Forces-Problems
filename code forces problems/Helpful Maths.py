maths=list(map(int,input().split('+')))
maths=sorted(maths)
for j in range(len(maths)) :
    if j<len(maths)-1:
        print(maths[j],end='+')
    else:
        print(maths[j])
