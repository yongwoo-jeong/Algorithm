case = input()
cnt = 0

letter = [chr(i+65) for i in range(26)]

for l in case:
    if l in letter[0:3]:
        cnt+=3
    elif l in letter[3:6]:
        cnt+=4
    elif l in letter[6:9]:
        cnt+=5
    elif l in letter[9:12]:
        cnt+=6
    elif l in letter[12:15]:
        cnt+=7
    elif l in letter[15:19]:
        cnt+=8
    elif l in letter[19:22]:
        cnt+=9
    elif l in letter[22:26]:
        cnt+=10

print(cnt)
        
        