rString=input()
for i in rString:
    if i in ['A','a','E','e','I','i','O','o','U','u','Y','y']:
        rString = rString.replace(i,"")
rString=rString.lower()
rString='.'.join(rString)
rString='.'+rString
print(rString)