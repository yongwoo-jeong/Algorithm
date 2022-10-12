import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = [] # list for PRINT

is_fail = 0

cur = 1
for i in range(n):
    num = int(input())
    while cur<=num:
        stack.append(cur)
        answer.append("+")
        cur +=1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        is_fail = 1
        break

if is_fail == 0:
    for i in answer:
        print(i)