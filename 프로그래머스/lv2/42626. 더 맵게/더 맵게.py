from heapq import heapify, heappop, heappush


def solution(scoville, k):
    heapify(scoville)
    answer = 0
    while True:
        if len(scoville) < 2:
            break
        minimum_first, minimum_next = heappop(scoville), heappop(scoville)
        heappush(scoville, minimum_first+minimum_next*2)
        if minimum_first >= k:
            break
        answer += 1
    if scoville[0] < k:
        return -1
    else:
        return answer