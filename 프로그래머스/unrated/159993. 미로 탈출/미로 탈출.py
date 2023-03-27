from collections import deque


def bfs(start, end, maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    length = len(maps[0])
    height = len(maps)
    visited = [[False]*length for _ in range(height)]
    que = deque()
    start_found = False

    for i in range(height):
        for j in range(length):
            if maps[i][j] == start:
                que.append((i, j, 0))
                visited[i][j] = True
                start_found = True
                break
        if start_found:
            break

    while que:
        y, x, cost = que.popleft()
        if maps[y][x] == end:
            return cost
        for i in range(4):
            ny = y+dx[i]
            nx = x+dy[i]

            if 0 <= ny < height and 0 <= nx < length and maps[ny][nx] != 'X':
                if visited[ny][nx]==False:
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True

    return -1


def solution(maps):
    to_lever = bfs('S', 'L', maps)
    to_exit = bfs('L', 'E', maps)

    if to_lever != -1 and to_exit != -1:
        return to_exit+to_lever
    else:
        return -1
