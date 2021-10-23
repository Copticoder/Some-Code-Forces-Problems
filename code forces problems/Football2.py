team=input()
counter=1
for i in range(1,len(team)):
    if team[i] == team[i-1]:
        counter+=1
    else:
        counter=1
    if counter ==7:
        break
if counter ==7:
    print('YES')
else:
    print('NO')