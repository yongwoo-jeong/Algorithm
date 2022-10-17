import sys, ast
from collections import deque

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    # Get input string 
    funcs = input().strip()
    funcs = deque(list(funcs))
    # Get list size
    size = int(input())
    l = input().strip()
    l = ast.literal_eval(l)
    l = deque(l)
    # If "D" more than list size -> Error
    how_many_d = funcs.count("D")
    is_reversed = 0
    if size < how_many_d:
        print("error")
        continue
    elif size == how_many_d:
        print([])
        continue
    else:
        while funcs:
            func = funcs.popleft()
            if func =="R":
                if is_reversed == 0:
                    is_reversed = 1
                else:
                    is_reversed = 0
            else:
                if is_reversed == 0:
                    l.popleft()
                else:
                    l.pop()
    if is_reversed ==0:
        l = list(map(str, l))
        l = ",".join(l)
        print("["+l+"]")
    else:
        l.reverse()
        l = list(map(str, l))
        l = ",".join(l)
        print("["+l+"]")