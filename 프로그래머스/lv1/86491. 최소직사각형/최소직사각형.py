def solution(sizes):
    # 가로 , 세로를 더 큰걸로 갱신해나가기?
    # 바뀌는 경우는?
    x, y = [], []
    for s in sizes:
        x.append(max(s[0], s[1]))
        y.append(min(s[0], s[1]))
    answer = max(x)*max(y)
    return answer