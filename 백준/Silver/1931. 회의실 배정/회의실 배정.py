import sys

input = sys.stdin.readline

n = int(input())
confs = [list(map(int, input().split())) for _ in range(n)]
confs.sort(key= lambda x : (x[1],x[1]+x[0]))

holding = [confs[0]]
confs = confs[1:]

cnt = 0
tmp = []

for conf in confs:
    start = conf[0]
    end = conf[1]
    if start >= holding[-1][1]:
        holding.append(conf)
    else:
        tmp.append(conf)
        cnt +=1
        if cnt > 1 and end > tmp[-1][1]:
            confs.pop()
            confs += tmp
            cnt = 0
            tmp = []

print(len(holding))