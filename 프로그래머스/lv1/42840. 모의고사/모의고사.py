def solution(answers):
    one = [1, 2, 3, 4, 5]  # 5
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    l = len(answers)//5 + 1
    one = (one*l)[:len(answers)]
    two = (two*l)[:len(answers)]
    thr = (thr*l)[:len(answers)]
    one_cnt, two_cnt, thr_cnt = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            one_cnt += 1
        if answers[i] == two[i]:
            two_cnt += 1
        if answers[i] == thr[i]:
            thr_cnt += 1
    answer = [one_cnt, two_cnt, thr_cnt]
    m = max(answer)
    answer = [i+1 for i, v in enumerate(answer) if v == m]
    return answer