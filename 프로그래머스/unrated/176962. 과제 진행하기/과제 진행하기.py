from collections import deque


def solution(plans):
    answer = []
    for p in plans:
        h, m = map(int, p[1].split(":"))
        p[1] = h*60+m
        p[2] = int(p[2])
    plans = deque(sorted(plans, key=lambda x: x[1]))
    # 스택에는 과목명과 남은 시간만 저장 (시작시간은 불필요)
    stack = []
    sub, start, time = plans.popleft()
    while plans:
        next_sub, next_start, next_time = plans.popleft()
        work_time = start+time
        # 시간이 모자란 경우 스택에 저장
        if work_time > next_start:
            # 과목명, 남은 시간만 저장
            stack.append([sub, work_time-next_start])
            sub, start, time = next_sub, next_start, next_time
        # 시간 딱 맞으면 앞에건 종료
        elif work_time == next_start:
            answer.append(sub)
            sub, start, time = next_sub, next_start, next_time
        # 시간 남는 경우
        else:
            answer.append(sub)
            spare_time = next_start-work_time
            while stack:
                stack_sub, stack_time = stack.pop()
                if stack_time > spare_time:
                    stack.append([stack_sub, stack_time-spare_time])
                    break
                spare_time -= stack_time
                if spare_time <= 0:
                    answer.append(stack_sub)
                    break
                answer.append(stack_sub)
            sub, start, time = next_sub, next_start, next_time
    answer.append(sub)
    while stack:
        answer.append(stack.pop()[0])

    return answer