def solution(lottos, win_nums):
    corret_count = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)

    best = 7-corret_count-zero if corret_count+zero >= 2 else 6
    worst = 7 - corret_count if corret_count >= 2 else 6
    answer = [best, worst]

    return answer