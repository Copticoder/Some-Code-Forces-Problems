listInput=list(map(int,input().split()))
n, k, l, c, d, p, nl, np=listInput[0],listInput[1],listInput[2],listInput[3],listInput[4],listInput[5],listInput[6],listInput[7]
print(int(min((k*l)/nl,c*d,p/np)//n))