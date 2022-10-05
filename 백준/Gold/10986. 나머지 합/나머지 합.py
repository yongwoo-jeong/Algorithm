import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# 5 3
num_list = list(map(int, input().rstrip().split()))
# 1 2 3 1 2
prefix_sum = [0]
# Accum'd number
remainder_info = [0 for _ in range(m)]
# [0, 0, 0]
remainder_info[0] = 1
# [1, 0, 0]
total = 0
for i in range(n):
    # i = 0,1,2,3,4,
    total += num_list[i]
    prefix_sum.append(total)  # Accum'd number list
    r = total % m
    remainder_info[r] += 1  # Reminder will be Index

count = 0
for i in remainder_info:  # [나머지 0 - 4, 나머지 1 - 2, 0]
    count += i*(i-1) // 2  # 4*3 //2 + 2*1//2
print(count)