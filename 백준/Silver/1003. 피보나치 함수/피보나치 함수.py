from sys import stdin
from functools import lru_cache
input = stdin.readline

n = int(input())

@lru_cache(maxsize=None)
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for _ in range(n):
    number = int(input())
    if number == 0:
        print(1,0)
    else:
        print(fibonacci(number-1) ,fibonacci(number))