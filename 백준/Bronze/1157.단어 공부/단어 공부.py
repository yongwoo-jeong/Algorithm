case = list(map(str, input().lower()))
count = []
pair = {}

for i in set(case):
    numb = case.count(i)
    count.append(numb)
    pair[i] = numb
    
count.sort(reverse=True)
if len(count) == 1:
    print(case[0].upper())
elif count[0] == count[1]:
    print("?")
else:
    for key, value in pair.items():
        if value == count[0]:
            print(key.upper())
