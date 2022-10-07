
import sys
from collections import deque

input = sys.stdin.readline
number = deque(list(range(int(input().strip()),0,-1)))
while True:
    if len(number) ==1:
        break    
    number.pop()
    number.appendleft(number.pop())

print(number[0])