word = input()
output = []
for i in range(26):
    breaker = False
    target = chr(i+97)
    for index, a in enumerate(word):
        if target == a:
            output.append(word.index(a))
            breaker = True
            break
        else:
            if index == len(word)-1:
                output.append(-1)
            else:
                pass
    if breaker == True:
        pass
answer = " ".join(str(s) for s in output)            
print(answer)
