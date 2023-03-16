def solution(cap, n, deliveries, pickups):
    answer = 0
    del_cnt = 0
    pick_cnt = 0

    for i in range(n):
        del_cnt += deliveries[n-i-1]
        pick_cnt += pickups[n-i-1]

        while del_cnt > 0 or pick_cnt > 0:
            del_cnt -= cap
            pick_cnt -= cap
            answer += n-i
    return answer*2