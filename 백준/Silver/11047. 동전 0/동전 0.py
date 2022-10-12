import sys

input = sys.stdin.readline

coin, goal = map(int,input().split())
coins = [int(input()) for x in range(coin) if x <= goal]
coins = coins[::-1]

cnt = 0
i = 0

# Find element biggest under goal
while goal > 0:
    for i in coins:
        if i <= goal:
            share = goal // i
            goal -= share*i
            cnt+= share
            break
    
print(cnt)