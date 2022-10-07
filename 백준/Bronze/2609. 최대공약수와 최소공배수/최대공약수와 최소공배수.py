
import sys
from collections import deque

input = sys.stdin.readline
a, b = map(int, input().split())

if a>b:
    multiply = a*b
    while b>0:
        a, b = b, a%b
    print(a)
    print(int(multiply/a))
elif a<b:
    multiply = a*b
    while a>0:
        b, a = a, b%a
    print(b)
    print(int(multiply/b))
else:
    print(a)
    print(a)