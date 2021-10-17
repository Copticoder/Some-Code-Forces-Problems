from math import sqrt
areas= list(map(int,input().split(' ')))
edge1 = sqrt((areas[0]*areas[1])/areas[2])*4
edge2=sqrt((areas[0]*areas[2])/areas[1])*4
edge3=sqrt((areas[2]*areas[1])/areas[0])*4
sumEdg=edge1+edge2+edge3
print(int(sumEdg))