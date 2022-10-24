from sys import stdin
input = stdin.readline

n,m  = map(int, input().split())
first = []
for _ in range(n):
    first.append(list(map(int, input().split())))


m,k = map(int, input().split())
sec = []
for _ in range(m):
    sec.append(list(map(int, input().split())))

answer = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        answer[i][j] = 0 # if 0, 0 
        for x in range(m):
            answer[i][j] += first[i][x]*sec[x][j]

for i in answer:
    i = list(map(str, i))
    print(" ".join(i))