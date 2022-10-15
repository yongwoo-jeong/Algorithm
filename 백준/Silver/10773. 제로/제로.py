import sys
# from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    number = int(input())
    if number:
        numbers.append(number)
    else:
        numbers.pop()

print(sum(numbers))
    