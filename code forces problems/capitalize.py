word=list(input())
if ord(word[0])>96:
    word[0]=chr(ord(word[0])-32)
for j in word:
    print(j,end='')