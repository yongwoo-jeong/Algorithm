def solution(k, d):
    # 원점
    answer = 0
    for i in range(0, d+1, k):
        coords = int((d**2 - i**2) ** 0.5)
        # 모든 좌표중 k 배수인 점만 (세로만 생각하면 된다. (0,0) (0,2) (0,4) 순으로 찍히니까 )
        answer += coords//k +1
    return answer
