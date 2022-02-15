N = int(input())
not_equal = set()

for i in range(1, N+1):
    number = list(map(int, str(i)))
    degit = len(number)
    if degit == 1 or degit == 2:
        pass
    else:  
        for n in range(degit-2):
            if number[n] - number[n+1] != number[n+1] - number[n+2]:
                not_equal.add(i)
                break
         
count = N - len(not_equal)
print(count)