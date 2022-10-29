from sys import stdin
from collections import defaultdict
input = stdin.readline

n, m = map(int, input().split())
mbers = defaultdict(int)

for _ in range(n):
    mbers[input().strip()] += 1

for _ in range(m):
    mbers[input().strip()] += 1

answer = [x for x in mbers.keys() if mbers[x] == 2]
answer.sort()
print(len(answer))
for i in answer:
    print(i)