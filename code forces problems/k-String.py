k=int(input())
text=input()
text=sorted(text)
letters=[[] for _ in range(26)]
j=0
while len(text) and j < len(letters):
    i=text[0]
    while len(text) and text[0] == i:
        letters[j].append(text.pop(0))
    j+=1
x =0
while x<len(letters) and letters[x]:
    x+=1
cant=False
letters=letters[0:x]
lengths=([len(x) for x in letters])
minLeng=min(lengths)
for z in lengths:
    if z % k !=0:
        cant=True
        break
if cant:
    print(-1)
else:
    for o in range(minLeng):
        for p in range(len(letters)):
            for l in range(len(letters[p])//k):
                print(letters[p][l],end='')


