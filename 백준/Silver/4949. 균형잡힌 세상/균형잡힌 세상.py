import sys
from collections import deque

input = sys.stdin.readline

while True:
    sentence = [x for x in input().rstrip()]
    if sentence == ["."]:
        break
    sentence = deque([x for x in sentence if x in ["(", ")", "[", "]"]])
    stack = []
    is_no = 0
    while sentence:
        check = sentence.popleft()
        if check == "(":
            stack.append(")")
        elif check == "[" :
            stack.append("]")
        else:
            try:
                top = stack.pop()
                if top == check:
                    continue
                else:
                    is_no=1
            except:
                is_no = 1
                break
    if is_no:
        print("no")
    else:
        if stack:
            print("no")
        else:
            print("yes")
        

           