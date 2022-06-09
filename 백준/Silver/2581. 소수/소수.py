min = int(input())
max = int(input())
prime =[]
cand = list(range(min,max+1))

for i in cand:
    divisor = []    
    if i == 1:
        pass
    elif i == 2:
        prime.append(2)
        pass
    else:
        for j in range(2,i):
            if i%j == 0:
                divisor.append(j)
            else:
                pass
    if divisor==[]:
        if i == 1 or i == 2:
          pass
        else:
          prime.append(i)
    else:
        pass

if prime == []:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
