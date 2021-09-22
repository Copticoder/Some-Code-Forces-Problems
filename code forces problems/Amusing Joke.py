frst,scnd=input(),input()
pile=input()
pile,third=sorted(pile),sorted(frst+scnd)
if third==pile:
    print('YES')
else:
    print('NO')