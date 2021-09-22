numQu,*time=input().split(' ')
stringQu=list(map(str,input()))
time=int(*time)
i=0
genQue=[]
while time>0:
    while i<len(stringQu):
        if i< len(stringQu)-1:
            if stringQu[i]=='B' and stringQu[i+1]=='G':
                stringQu[i]='G'
                stringQu[i+1]='B'
                i+=1
        i+=1
    time-=1
    i=0
for j in stringQu:
    print(j,end='') 

#  B  G  G  B  G
# GBGGB 
# BGGBG 
# GBGGB 
# GGBGB 