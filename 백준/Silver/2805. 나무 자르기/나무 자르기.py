import sys
# from collections import deque

input = sys.stdin.readline

n, need = map(int,input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start+end)//2
    cut = [x-mid for x in trees if x>mid]
    cut = sum(cut)
    if cut >= need:
        start = mid+1
    else:
        end = mid -1

print(end)
