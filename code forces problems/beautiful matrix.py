rows=5
matrix=[]
while rows:
    matrixRow=list(map(int,input().split(' ')))
    matrix.append(matrixRow)
    rows-=1

for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            num=(abs(i-2))+(abs(j-2))
            print(num)
            break