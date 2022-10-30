from sys import stdin
import heapq
input = stdin.readline

n = int(input())
h = []
for _ in range(n):
    number = int(input())
    if number == 0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, number)