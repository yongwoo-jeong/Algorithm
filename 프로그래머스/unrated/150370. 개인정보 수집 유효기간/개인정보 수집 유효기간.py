def solution(today, terms, privacies):
    answer = []
    # 약관 dict
    expire_year, expire_month, expire_day = map(int, today.split('.'))
    terms_dict = {x.split()[0]: int(x.split()[1])*28 for x in terms}
    for i, p in enumerate(privacies):
        start, term = p.split()
        start_year, start_month, start_day = map(int, start.split('.'))
        year_gap = (expire_year-start_year)*12
        month_gap = (year_gap+expire_month - start_month)*28
        day_gap = month_gap+expire_day - start_day
        if day_gap >= terms_dict[term]:
            answer.append(i+1)

    return answer