def solution(wallpaper):
    answer = []
    width = []
    height = []
    max_row = len(wallpaper)
    max_col = len(wallpaper[0])

    for i in range(max_row):
        for j in range(max_col):
            if wallpaper[i][j] == "#":
                width.append(i)
                height.append(j)
    answer.append(min(width))
    answer.append(min(height))
    answer.append(max(width)+1)
    answer.append(max(height)+1)

    return answer