import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())
q = deque()
answer = []

for i in range(1,n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

answer = [str(x) for x in answer]
print(f"<{', '.join(answer)}>")
