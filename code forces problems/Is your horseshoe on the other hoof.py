horseshoe=list(map(int,input().split(' ')))
horseshoe=sorted(horseshoe)
counter = sum(horseshoe[i] == horseshoe[i-1] for i in range(1,len(horseshoe)))
print(counter)


