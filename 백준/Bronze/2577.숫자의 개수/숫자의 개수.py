a = int(input())
b = int(input())
c = int(input())
numb = list(map(int,str(a*b*c)))
for i in range(10):
    print(numb.count(i))