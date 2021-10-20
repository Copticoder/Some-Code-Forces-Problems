text=input()
length=len(text)
counter =0
magic=True
while length:
    if text[counter : counter +3] =='144':
        counter +=3
        length-=3
    elif text[counter:counter+2]=='14':
        counter +=2 
        length-=2
    elif text[counter]=='1':
        counter +=1
        length-=1
    else:
        magic=False
        break
if magic:
    print('YES')
else:
    print('NO')
