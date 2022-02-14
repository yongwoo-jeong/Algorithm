import sys
case = int(input())
for i in range(case):
    data = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    ppl = data.pop(0)
    avg_score = sum(data) / ppl
    for s in data:
        if s > avg_score:
            cnt +=1
        else:
            pass
    print(f"{cnt/ppl*100:.3f}%")