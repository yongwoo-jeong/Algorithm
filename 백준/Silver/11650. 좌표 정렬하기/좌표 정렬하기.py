import sys
input = sys.stdin.readline

times =  int(input())

cords = []
for _ in range(times):
    cord = input().strip()
    cords.append(cord)

cords.sort(key=lambda x: (int(x.split()[0]), (int(x.split()[1]))))

for i in cords:
    print(i)