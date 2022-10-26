import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)


T = int(input())

def dfs(x:int, y:int):
    if x<0 or y<0 or x>=n or y>=m   or field[x][y] == 0:
        return
    field[x][y] = 0
    dfs(x,y+1)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x-1,y)

for _ in range(T):
    m,n,k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        field[y][x] = 1
    cnt = 0 
    for i in range(n): # 0~7
        for j in range(m): # 0~
            if field[i][j] == 1:
                dfs(i,j)
                cnt +=1
    print(cnt)