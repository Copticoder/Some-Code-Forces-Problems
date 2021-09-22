inpWord=input()
i=0
for x in inpWord:
    if x.isupper():
        i+=1
    else:
        i-=1
inpWord = inpWord.upper() if i >0 else inpWord.lower()
print(inpWord)
