import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
gases = list(map(int, input().split()))
gases.pop()

cheap = gases[0]
answer = 0
for i in range(len(gases)):
    if gases[i] < cheap:
        cheap = gases[i]
    answer += cheap*distance[i]

print(answer)
    