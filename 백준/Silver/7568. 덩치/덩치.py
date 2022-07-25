import sys

def compare():
    T = int(input())
    wh = []
    for i in range(T):
        w, h = map(int, sys.stdin.readline().split())
        wh.append([w,h])
        # wh = [[55,170],[60,175],[50,180]]
    for i in range(len(wh)):
        rank = 1
        for j in range(len(wh)):
            if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
                rank +=1
        print(rank, end=" ")
        
compare()
