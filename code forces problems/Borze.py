borzeCode=list(map(str,input()))
borzeList=[]
j=0
while j < len(borzeCode):
        if (borzeCode[j]=='-' and borzeCode[j+1]=='.') or (borzeCode[j]=='-' and borzeCode[j+1]=='-'):
            if borzeCode[j]=='-' and borzeCode[j+1]=='.':
                # borzeList.append(1)
                print(1,end='')
                j+=1
            else:
                print(2,end='')
                j+=1
        else:
            print(0,end='')
        j+=1