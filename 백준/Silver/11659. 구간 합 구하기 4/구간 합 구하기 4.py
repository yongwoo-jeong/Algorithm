import sys

N, times = map(int, sys.stdin.readline().split())
numbers = [int(i) for i in sys.stdin.readline().split()]
prefix = [0]
accum = 0

for i in numbers:
    accum = accum+i
    prefix.append(accum)

for i in range(times):
    start, end = map(int, sys.stdin.readline().split())
    answer = prefix[end] - prefix[start-1]
    print(answer)
