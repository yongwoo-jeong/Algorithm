import sys

a,b = map(int, sys.stdin.readline().split())
son = [x for x in range(1, a+1)]
mom_one = [x for x in range(1, a-b+1)]
mom_two = [x for x in range(1,b+1)]

head_num = 1
for i in son:
    head_num*=i

mom_one_num =1
mom_two_num =1

for i in mom_one:
    mom_one_num *= i

for i in mom_two:
    mom_two_num *= i

print(int(head_num /(mom_one_num*mom_two_num)))
