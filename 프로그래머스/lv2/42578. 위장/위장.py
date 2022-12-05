from itertools import combinations
from collections import defaultdict


def solution(clothes):
    answer = 1
    integrate = defaultdict(list)
    for i in clothes:
        name, type = i
        integrate[type].append(name)
    for _, v in integrate.items():
        v.append("")
        c = combinations(v, 1)
        answer *= sum(1 for _ in c)
    return answer-1