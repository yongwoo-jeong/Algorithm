from sys import stdin
input = stdin.readline

n = int(input())
video = []

for _ in range(n):
    video.append(list(map(int, input().split())))

minus = 0
zero = 0
one = 0
def check(x,y,n):
    global minus, zero, one
    number = video[x][y]
    to_quad = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if number != video[i][j]:
                to_quad = 1
                break
    if to_quad ==1:
        triple = n // 3
        check(x, y, triple)
        check(x, y+triple, triple)
        check(x, y+2*triple, triple)
        check(x+triple, y, triple)
        check(x+triple, y+triple, triple)
        check(x+triple, y+2*triple, triple)
        check(x+2*triple, y, triple)
        check(x+2*triple, y+triple, triple)
        check(x+2*triple, y+2*triple, triple)
    else:
        if number == 1:
            one += 1
        elif number == 0:
            zero += 1
        else:
            minus += 1
        return

check(0,0,n)
print(minus)
print(zero)
print(one)

