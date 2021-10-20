ber=input()
bir=input()
if len(ber)!=len(bir):
    print('NO')
else:
    transBool=True
    for i in range(len(ber)):
        if ber[i] != bir[len(ber)-1-i]:
            transBool=False
            break
    if transBool:
        print('YES')
    else:
        print('NO')