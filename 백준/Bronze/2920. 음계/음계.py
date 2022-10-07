n = list(map(int,input().split()))

a = list(range(1,9))
d = list(range(8,0,-1))

if n == a:
    print("ascending")
elif n == d:
    print("descending")
else:
    print("mixed")