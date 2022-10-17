import sys
#from collections import deque

input = sys.stdin.readline
n = int(input())
numbs =  [0 for x in range(10001)]
for _ in range(n):
    target = int(input())
    numbs[target] +=1

for i,x in enumerate(numbs):
    if x == 0:
        continue
    else:
        for _ in range(x):
            print(i)