import sys

board = [[0 for _ in range(100)] for _ in range(100)]
for t in range(4):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1

cnt = 0
for i in range(len(board)):
    cnt += sum(board[i])
print(cnt)