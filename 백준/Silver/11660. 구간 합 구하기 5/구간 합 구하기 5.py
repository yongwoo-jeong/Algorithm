import sys

input = sys.stdin.readline
n, m = map(int,input().split())
l = [[0]*(n+1)]

for _ in range(n):
    tmp = [0] + list(map(int, input().split()))
    l.append(tmp)

for i in range(1,n+1):
    for j in range(1,n):
        l[i][j+1] += l[i][j]

for i in range(1, n+1):
    for j in range(1,n):
        l[j+1][i] += l[j][i]

for _ in range(m):
    s_row, s_index, e_row, e_index = map(int, input().split())
    answer = l[e_row][e_index] - l[s_row-1][e_index] - l[e_row][s_index-1] + l[s_row-1][s_index-1]
    print(answer)