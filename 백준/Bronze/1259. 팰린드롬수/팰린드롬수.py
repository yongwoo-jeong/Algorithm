import sys

input = sys.stdin.readline
l = []

while True:
    target = input().strip()
    flag = 0
    if target =="0":
        break
    for i in range(1, len(target)//2+1):
        l = target[-i]
        r = target[-len(target)+i-1]
        if l!=r:
            print("no")
            flag = 1
            break
    if flag:
        continue
    else:
        print("yes")