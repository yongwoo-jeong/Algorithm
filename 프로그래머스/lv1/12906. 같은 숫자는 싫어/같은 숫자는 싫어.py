from collections import deque


def solution(arr):
    arr = deque(arr)
    answer = [-1]
    while arr:
        target = arr.popleft()
        if answer[-1] != target:
            answer.append(target)
    answer.remove(-1)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer