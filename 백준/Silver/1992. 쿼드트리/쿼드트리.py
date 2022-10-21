from sys import stdin
input = stdin.readline

n = int(input())
video = []

for _ in range(n):
    video.append(list(map(int, input().strip())))

answer = ""
def check(x,y,n):
    global answer
    color = video[x][y]
    to_quad = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != video[i][j]:
                to_quad = 1
                break
    if to_quad ==1:
        answer += "("
        check(x, y, n // 2)
        check(x, y + n // 2, n // 2)
        check(x + n // 2, y, n // 2)
        check(x + n // 2, y + n // 2, n // 2)
        answer += ")"
    else:
        if color == 1:
            answer += "1"
        else:
            answer += "0"
        return

check(0,0,n)
print(answer)
