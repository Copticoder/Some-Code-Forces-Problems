n=int(input())
teams=[]
counters=[0]*n
while n:
    team=input()
    if team in teams:
        counters[teams.index(team)]+=1
    else:
        teams.append(team)
    n-=1
print(teams[counters.index(max(counters))])