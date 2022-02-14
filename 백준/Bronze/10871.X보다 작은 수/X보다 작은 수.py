N, X = map(int, input().split())
numbs = list(map(int,input().split()))
new_list = []

for i in numbs:
    if i < X:
        new_list.append(i)
    else:
        pass
new_list = ' '.join(str(s) for s in new_list)
print(new_list)