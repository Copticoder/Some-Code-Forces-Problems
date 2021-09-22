n=int(input())
heights=list(map(int,input().split(' ')))
min=max(heights)
tracker=0
for i in range(len(heights)):
    if min>=heights[i]:
        min=heights[i]
        tracker=i
print(abs(tracker-(len(heights)-1))+abs(heights.index(max(heights))-(len(heights)-1)-1))
print(tracker)
print(heights.index(max(heights)))
