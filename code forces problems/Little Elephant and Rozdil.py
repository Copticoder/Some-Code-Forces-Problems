n=int(input())
cities=list(map(int,input().split()))
smallest=cities[0]
isStill=False
for i in range(1,len(cities)):
    if smallest == cities[i]:
        isStill=True
    if smallest > cities[i]:
        isStill=False
        smallest = cities[i]
if isStill:
    print("Still Rozdil")
else:
    print(cities.index(smallest)+1)
