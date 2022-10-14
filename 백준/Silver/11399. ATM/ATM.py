import sys
# from collections import deque

input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))
people.sort()

accm = 0
accm_time = []
for i in people:
    accm += i
    accm_time.append(accm)
print(sum(accm_time))