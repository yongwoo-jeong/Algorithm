def solution(n, m, section):
    answer = 0
    wall = [1 for x in range(n+1)]
    for i in section:
        wall[i] = 0

    # 전부 칠해지면 리스트는 모두 1
    while (0 in wall):
        #   탐색중 0을만나면 앞의 1은 전부 날려버리면 탐색이빨라질듯
        # 첫번째는 인덱싱을 위한 1이 존재. 포인터는 1부터 시작
        pointer = 0
        for i in range(len(wall)):
            if wall[i] == 0:
                pointer = i
                break
        answer += 1
        wall = wall[pointer:]
        wall[0:m] = [1 for x in range(m)]
    return answer