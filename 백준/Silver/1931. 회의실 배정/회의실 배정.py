import sys

input = sys.stdin.readline

n = int(input())
confs = [list(map(int, input().split())) for _ in range(n)]
confs.sort(key= lambda x : (x[1], x[0]))

cnt = 1

end = confs[0][1]
for i in range(1,n):
    if confs[i][0] >= end:
        cnt+=1
        end = confs[i][1]

print(cnt)