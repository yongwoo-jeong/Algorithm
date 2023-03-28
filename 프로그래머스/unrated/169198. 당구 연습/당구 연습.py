def solution(m, n, startX, startY, balls):
    answer = []
    cushion_points = []
    cushion_points.append([-startX, startY])
    cushion_points.append([2*m-startX, startY])
    cushion_points.append([startX, -startY])
    cushion_points.append([startX, 2*n-startY])

    for cords in balls:
        goalX, goalY = cords
        length = 0
        height = 0
        distances = []
        for point in cushion_points:
            pointX, pointY = point
            # 쿠션 전에 만나는 경우는 continue
            if pointY == goalY:
                if pointX < goalX < startX or startX < goalX < pointX:
                    continue
            if pointX == goalX:
                if pointY < goalY < startY or startY < goalY < pointY:
                    continue

            if goalX > pointX:
                length = goalX-pointX
            else:
                length = pointX-goalX
            if goalY >= pointY:
                height = goalY-pointY
            else:
                height = pointY-goalY

            distances.append(length**2+height**2)
        answer.append(min(distances))
    return answer
