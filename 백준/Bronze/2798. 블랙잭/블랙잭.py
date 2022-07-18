import sys
from bisect import bisect_left, bisect_right

cards, goal = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sum_list = []

# 리스트 내 전체 요소 3개씩 뽑고 더한 후 새로운 리스트에 담아주기.
# 그 과정에서 goal과 비교 후 동일한 값이 나오면 즉시 종료
# 나오지 않을 경우 리스트 내 이진탐색으로 가장 근접한 값 출력.


def blackjack(goal, numbers):
    global sum_list
    # 리스트 내 포인터역할
    first = 0
    second = first+1
    third = first+2
    while True:
        # 최소 3개의 조합이 나와야하므로 마지막 3개의 합이 마지막 경우의 수
        # first 포인터가 인덱스 [-3]에 위치하면 마지막 합계 더하고 종료
        if first == len(numbers)-3:
            sum_value = numbers[first] + numbers[second] + numbers[third]
            sum_list.append(sum_value)
            break
        # third 인덱스가 리스트 마지막 값까지 가도록
        if third < len(numbers):
            sum_value = numbers[first] + numbers[second] + numbers[third]
            sum_list.append(sum_value)
            third += 1
        else:
            # third가 길이를 초과할 경우 second 증가
            if second < len(numbers)-1:
                second += 1
                third = second + 1
            else:
                # second도 초과할 경우 first 증가
                first += 1
                second = first+1
                third = first+2
    if goal in sum_list:
        print(goal)
    else:
        sum_list = sorted(sum_list)
        try:
            target = bisect_left(sum_list, goal)-1
            left = sum_list[target]
            right = sum_list[target+1]
            print(left if target-left < right-target else right)
        except:
            print(sum_list[-1])


blackjack(goal, numbers)