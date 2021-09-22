n=int(input())
wordList=[]
while n:
    word=input()
    wordList.append(word)
    n-=1
counter=1
resultList=[]
for i in wordList:
    for _ in range(1,len(i)-2):
        counter+=1
    if counter >8:
        resultList.append(i[0]+str(counter)+i[-1])
    else:
        resultList.append(i)
    counter=1
for z in resultList:
    print(z)

