from collections import deque


def solution(x):
    callList = x.splitliness()[1:]
    #리스트로 반환
    graph = {}
    # 그래프 완성) 리스트-> 반복문으로 각 항목 맨 앞 값이 key가 되는 dict 의 리스트로 변환
    for call in callList:
        eachList = call.split(())
        graph[eachList[0]] = eachList[1:]
    
    search_que = deque()
    search_que += graph[1]

    while search_que:
        person = search_que.popleft()