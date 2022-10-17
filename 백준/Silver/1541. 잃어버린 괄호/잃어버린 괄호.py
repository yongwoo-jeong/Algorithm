import sys
from collections import deque

input = sys.stdin.readline
math = input().strip()
math_list = []
number = ""
for i in math:
    if i == "+" or i == "-":
        math_list.append(number)
        number = ""
        math_list.append(i)
    else:
        number+=i
math_list.append(number)

answer = 0
is_minus = 0 
for i in math_list:
    if i !="+" and i !="-":
        i = int(i)
        if is_minus:
            answer -= i
        else:
            answer += i
    else:
        if i == "-":
            is_minus = 1

print(answer)