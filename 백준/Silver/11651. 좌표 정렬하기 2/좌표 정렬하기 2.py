import sys
#from collections import deque

input = sys.stdin.readline
n = int(input())

cords = []
for _ in range(n):
    cord = input().strip()
    cords.append(cord)

cords.sort(key=lambda x:(int(x.split()[1]),int( x.split()[0])))
for i in cords:
    print(i)
