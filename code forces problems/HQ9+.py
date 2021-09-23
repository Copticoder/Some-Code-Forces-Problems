inst=input()
bol = any(i in ['H','Q','9'] for i in inst)
if bol:
    print('YES')
else:
    print('NO')