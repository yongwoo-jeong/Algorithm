r_list = []
for i in range(10):
    numb = int(input()) % 42
    r_list.append(numb)

r_list = list(set(r_list))
print(len(r_list))