import sys
input = sys.stdin.readline

MAX_H = 256
MIN_H = 0

N, M, B = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
# 가능한 높이 인덱스리스트 초기화
height_cnt = [0 for _ in range(MAX_H+1)] # 길이 = 256
answer_cost = 10000000001
answer_height = 0
sum_height = B

for row in board:
    for val in row:
        height_cnt[val] +=1
        sum_height += val


min_h = min([min(row) for row in board]) # 63
max_h = sum_height//(M*N) # 64
            
for h in range(min_h, max_h+1): # 필드 내 최소높이
    cost = 0 # == 시간
    usable_blocks =B  # 인벤토리
    for i in range(MIN_H, MAX_H+1): # 가능한 높이(정답)범위
        if h < i:
            cost += height_cnt[i] * abs(h-i) * 2
            usable_blocks += height_cnt[i] * abs(h-i)
        else:
            cost += height_cnt[i] * abs(h-i)
            usable_blocks -= height_cnt[i] * abs(h-i)

    if cost <= answer_cost and usable_blocks >= 0:
        answer_cost = cost
        answer_height =h
    
print(answer_cost, answer_height)