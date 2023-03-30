def solution(park, routes):
    col_limit = len(park)
    row_limit = len(park[0])
    # 강아지 현재위치
    posX = 0
    posY = 0
    for i, road in enumerate(park):
        if "S" in road:
            posY = i
            posX = road.index("S")
            break
    for route in routes:
        direction, step = route.split()
        step = int(step)
        try:
            # 북쪽이동
            if direction == "N":
                # 지도에서 벗어나는 경우 스킵
                if posY-step < 0:
                    continue
                # 경로에 장애물이 있는 경우
                if "X" in [x[posX] for x in park[posY-step:posY+1]]:
                    continue
                posY -= step
            # 동쪽
            if direction == "E":
                if posX+step >= row_limit:
                    continue
                if "X" in park[posY][posX:posX+step+1]:
                    continue
                posX += step
            if direction == "S":
                if posY+step >= col_limit:
                    continue
                if "X" in [x[posX] for x in park[posY:posY+step+1]]:
                    continue
                posY += step
            if direction == "W":
                if posX-step < 0:
                    continue
                if "X" in park[posY][posX-step:posX+1]:
                    continue
                posX -= step
        except:
            continue
    return [posY, posX]