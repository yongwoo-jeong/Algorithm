N = int(input())

def drawing_star(n):
    if n == 1:
        return ["*"]
    div3 = n//3
    stars = drawing_star(div3)
    new_list = []
    for s in stars:
        new_list.append(s*3)
    for s in stars:
        new_list.append(s+" "*div3+s)
    for s in stars:
        new_list.append(s*3)
    return new_list


print('\n'.join(drawing_star(N)))