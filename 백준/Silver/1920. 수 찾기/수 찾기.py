
import sys
import bisect

input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int,input().split()))
numbers.sort()

answers = int(input().strip())
cands = list(map(int,input().split()))

for i in cands:
    if i<numbers[0]:
        print(0)
    elif i > numbers[-1]:
        print(0)
    else:
        bi = bisect.bisect_left(numbers, i)
        if numbers[bi] == i:
            print(1)
        else:
            print(0)