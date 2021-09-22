x=3
buttons=[]
lights = [[1,1,1] for _ in range(3)]
while x:
    buttonPress=list(map(int,input().split(' ')))
    buttons.append(buttonPress)
    x-=1
for l in range(3):
    for m in range(3):
        lights[l][m]+=buttons[l][m]
        if l > 0:
            lights[l-1][m]+=buttons[l][m]
        if l < 2:
            lights[l+1][m]+=buttons[l][m]
        if m < 2:
            lights[l][m+1]+=buttons[l][m]
        if m > 0:
            lights[l][m-1]+=buttons[l][m]
for i in range(3):
    for j in range(3):
        lights[i][j] = 0 if lights[i][j] %2 == 0 else 1
        print(lights[i][j], end='')
    print('')