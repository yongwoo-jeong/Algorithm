import collections
import sys

# Should solve with double list
b_row, b_clm = map(int, input().split())
board = ""
answer_cand = []

for i in range(b_row):
    each_row = sys.stdin.readline().strip() + " "
    board = board+each_row
board = [[i for i in str(j)] for j in board.split()]
new_board = [[c for c in mini[0:4]] for mini in board[0:8]]
# Code for making into 2nd dinmensional list

# Code for comparing
first_pattern = "WBWBWBWB".split()
second_pattern = "BWBWBWBW".split()
s_one = (first_pattern+second_pattern)*4
s_two = (second_pattern+first_pattern)*4
# Code for making into 2nd dinmensional list
s_one = [[i for i in str(j)] for j in s_one]
s_two = [[i for i in str(j)] for j in s_two]
# Append Each row to Board


def search(target: list):
    one_cnt = 0
    two_cnt = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if target[i][j] != s_one[i][j]:
                one_cnt += 1
            if target[i][j] != s_two[i][j]:
                two_cnt += 1

    return one_cnt if one_cnt < two_cnt else two_cnt


row_init = 0
clm_init = 0
for i in range(0, b_row-7):
    for j in range(0, b_clm-7):
        new_board = [[c for c in mini[j:j+8]] for mini in board[i:i+8]]
        # new_board = [[c for c in str(mini)[0:8]] for mini in board[0:8]]
        answer_cand.append(search(new_board))

print(min(answer_cand))
