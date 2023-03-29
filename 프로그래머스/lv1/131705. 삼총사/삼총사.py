def solution(number):
    answer = 0
    for index, number_one in enumerate(number):
        for number_set in [(i, x) for i, x in enumerate(number) if i > index]:
            index_two, number_two = number_set
            for number_three in [x for i, x in enumerate(number) if i > index_two]:
                sum_all = number_one+number_two+number_three
                if sum_all == 0:
                    answer += 1

    return answer