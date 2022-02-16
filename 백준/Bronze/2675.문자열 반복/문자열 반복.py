import sys

case = int(input())
for i in range(case):
    answer = []
    time, word =  map(str, sys.stdin.readline().split())
    time = int(time)
    for w in word:
        answer.append(w*time)
    print("".join(answer))