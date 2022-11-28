from collections import defaultdict


def solution(nums):
    pmon = defaultdict(int)
    pick = len(nums)//2
    for i in nums:
        pmon[i] += 1
    if len(pmon.keys()) <= pick:
        return len(pmon.keys())
    else:
        return pick
