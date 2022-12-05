def solution(citations):
    citations.sort()
    answer = []
    for i in range(max(citations)+1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            answer.append(i)
    if answer == []:
        return 0
    else:
        return max(answer)