
import sys

input = sys.stdin.readline

time = int(input().strip())
answer = []
for _ in range(time):
    n = int(input().strip())
    answer.append(n)

answer.sort()
for i in answer:
    print(i)