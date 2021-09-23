frst,scnd=input().lower(),input().lower()
lex1,lex2=0,0
for i in range(len(frst)):
    if frst[i]==scnd[i]:
        continue
    elif ord(frst[i])>ord(scnd[i]):
        lex1+=1
        break
    else:
        lex2+=1
        break
if lex1==lex2:
    print(0)
elif lex1<lex2:
    print(-1)
else:
    print(1)
