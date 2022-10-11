import sys
input = sys.stdin.readline

stack = []
def push(x):
    stack.append(x)
def pop():
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
def top():
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