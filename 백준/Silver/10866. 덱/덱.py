import sys
#from collections import deque
input = sys.stdin.readline

stack = []
def push_front(x):
    stack.insert(0, x)
def push_back(x):
    stack.append(x)
def pop_front():
    if stack:
        tmp = stack[0]
        print(tmp)
        del stack[0]
    else:
        print(-1)
def pop_back():
    if stack:
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if stack:
        print(0)
    else:
        print(1)
def front():
    if stack:
        print(stack[0])
    else:
        print(-1)
def back():
    if stack:
        print(stack[-1])
    else:
        print(-1)
    
times = int(input())
for _ in range(times):
    calculation = input().split()
    if len(calculation) == 1:
        locals()[calculation[0]]()
    else:
        func = calculation[0]
        arg = (calculation[1])
        locals()[func](arg)
    