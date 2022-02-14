list = []
while True:
    try:
        list.append(int(input()))
    except:
        break
print(max(list))
print(list.index(max(list))+1)
    