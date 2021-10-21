n=int(input())
soldiers=list(map(int,input().split()))
lowestDiff=abs(soldiers[0]-soldiers[1])
stepper=0
for i in range(0,len(soldiers)):
    if i == len(soldiers)-1:
        if lowestDiff > abs(soldiers[i] - soldiers[0]):
            stepper=len(soldiers)-1
    elif lowestDiff > abs(soldiers[i]-soldiers[i+1]):
        lowestDiff=abs(soldiers[i]-soldiers[i+1])
        stepper=i
if stepper == len(soldiers)-1:
    print(1,stepper+1)
else:
    print(stepper+1,stepper+2)