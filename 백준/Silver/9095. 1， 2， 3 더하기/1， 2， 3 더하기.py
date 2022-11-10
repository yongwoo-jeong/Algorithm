from sys import stdin
input = stdin.readline

n = int(input())

igntn = [0, 1, 2, 4]
while len(igntn) < 11:
    new = igntn[-1]+igntn[-2]+igntn[-3]
    igntn.append(new)


for _ in range(n):
    number = int(input())
    print(igntn[number])