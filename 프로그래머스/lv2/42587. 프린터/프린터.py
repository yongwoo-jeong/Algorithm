from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    # 초기 인덱스 0~n 까지 정해준다음 이를 수정
    current_index = deque([i for i in range(len(priorities))])
    # 큐 통해서 인쇄순차를 뽑는건 쉬운데, location 을 어떻게 확인할지?
    while priorities:
        front_numb = priorities.popleft()
        front_index = current_index.popleft()
        if priorities == deque():
            answer += 1
            break
        # 높은 우선순위가 있을 경우
        if max(priorities) > front_numb:
            priorities.append(front_numb)
            current_index.append(front_index)
            continue
        # 더 높은 우선순위가 없다면 인쇄
        answer += 1
        # 팝레프트가 해당 인덱스일경우
        if front_index == location:
            break

    return answer
