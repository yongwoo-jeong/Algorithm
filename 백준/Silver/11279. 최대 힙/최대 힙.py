from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
heap = []
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heappush(heap, (-num, num))
    else:
        try:
            print(heappop(heap)[1])
        except:
            print(0)