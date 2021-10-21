song=input()
i=0
while song[i:i+3] == 'WUB':
    song=song[(i+3):]
song=song.split('WUB')
for i in song:
    print(i,end=' ')
