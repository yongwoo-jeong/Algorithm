def solution(board):
    board_list = [char for string in board for char in string]
    o_cnt = board_list.count('O')
    x_cnt = board_list.count('X')
    # x 카운트가 더 많은 경우
    if (o_cnt < x_cnt):
        return 0
    # o 카운트가 x보다 1 초과하여 많은 경우
    if (o_cnt-x_cnt > 1):
        return 0
    # 가로 틱택토
    for i in board:
        if len(set(i)) == 1:
            # 온점일 경우는 건너뛰기
            if i[0] == ".":
                continue
            if i[0] == "O":
                if o_cnt-x_cnt != 1:
                    return 0
            if i[0] == "X":
                if o_cnt-x_cnt != 0:
                    return 0

    # 세로 틱택토
    for i in range(3):
        target = board[0][i]
        # 온점일 경우는 건너뛰기
        if target == ".":
            continue
        cnt = 0
        for j in range(1, 3):
            if board[j][i] == target:
                cnt += 1
        if cnt == 2:
            if target == "O":
                if o_cnt-x_cnt != 1:
                    return 0
            if target == "X":
                if o_cnt-x_cnt != 0:
                    return 0
    # 대각 틱택토
    middle = board[1][1]
    left_accros = [board[0][0],  board[2][2]]
    right_accros = [board[0][2], board[2][0]]

    if len(set(left_accros)) == 1:
        if left_accros[0] == middle:
            if middle == "O":
                if o_cnt-x_cnt != 1:
                    return 0
            if middle == "X":
                if o_cnt-x_cnt != 0:
                    return 0
    if len(set(right_accros)) == 1:
        if right_accros[0] == middle:
            if middle == "O":
                if o_cnt-x_cnt != 1:
                    return 0
            if middle == "X":
                if o_cnt-x_cnt != 0:
                    return 0
    return 1
