from sys import stdin
input = stdin.readline

n = int(input())

b = [0, 1, 1, 2]
a = [0, 0, 1, 1]

if n <= 3:
    print(a[n], b[n])

else:
    for _ in range(n-3):
        nb = b[-1]+b[-2]
        na = a[-1]+a[-2]
        b.append(nb)
        a.append(na)
    print(a[-1], b[-1])
