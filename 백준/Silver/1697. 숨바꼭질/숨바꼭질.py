from sys import stdin
from collections import deque
input = stdin.readline
# 입력값 받기
n, k = map(int, input().split())
max_num = 100000
# 해당 위치에 도착한 시간
visited = [0] * (max_num+1)


def bfs():
    q = deque()
    q.append(n)  # 큐에 출발지점만
    while q:
        x = q.popleft()
        # q 안에는 이동한 위치가 들어있음
        # 그게 동생이랑 같다면 출력, 반복문종료
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_num and not visited[j]:
                # visited 인덱스 = 이동한 위치
                # visited[i] = 해당 위치까지 이동한 시간
                visited[j] = visited[x]+1
                q.append(j)


bfs()