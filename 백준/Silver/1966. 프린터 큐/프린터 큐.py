import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    numbers, target_i = map(int,input().split())
    imprtnt = deque(map(int, input().split()))
    i_list = deque([str(x) for x in range(numbers)])
    cnt = 0
    while imprtnt:
        biggest = max(imprtnt)
        front = imprtnt[0]
        if front >= biggest:
            tmp = i_list.popleft()
            imprtnt.popleft()
            cnt +=1
            if int(tmp) == target_i:
                break
        else:
            imprtnt.popleft()
            imprtnt.append(front)
            tmp = i_list.popleft()
            i_list.append(tmp)
    print(cnt)