
import sys
import collections

input = sys.stdin.readline

total = int(input().strip())
cards = list(map(int,input().split()))

number = int(input().strip())
numbers = list(map(int,input().split()))

counter = collections.Counter(cards)
answer = []
for n in numbers:
    if n in counter.keys():
        answer.append(counter[n])
    else:
        answer.append(0)
answer = [str(x) for x in answer]
answer =" ".join(answer)
print(answer)