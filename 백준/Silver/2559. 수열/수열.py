import sys

days, consec = map(int, input().split())
con_list = list(map(int, input().split()))

accum = sum(con_list[0:consec])
answer = [accum]

left = 0
right = consec

if consec == 1:
    print(max(con_list))
elif consec == days:
    print(sum(con_list))
else:
    while True:
        accum += con_list[right]
        accum -= con_list[left]
        answer.append(accum)

        left += 1
        right += 1
        if right == len(con_list):
            break
    print(max(answer))
