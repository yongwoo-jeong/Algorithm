from collections import defaultdict


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_count = defaultdict(int)
    report_name = defaultdict(list)
    for re in report:
        user_from, user_to = re.split()
        # 리폿한 네임 리스트에 들어있지 않은 경우만 신고누적 +1
        if user_to not in report_name[user_from]:
            report_count[user_to] += 1
        report_name[user_from].append(user_to)

    banned = [key for key, value in report_count.items() if value >= k]
    # 리포트네임 밸류를 빼서 세트변환후 교집합연산 -> 그 길이가  답이된다.
    for key, value in report_name.items():
        mail_count = (len((set(value) & set(banned))))
        i = id_list.index(key)
        answer[i] = mail_count

    return answer