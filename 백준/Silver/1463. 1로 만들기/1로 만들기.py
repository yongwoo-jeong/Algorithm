from sys import stdin
input = stdin.readline

n = int(input())
# dp list (d[i]은 i가 1이 되기위해 필요한 연산횟수)
d = [0] * (n+1)

for i in range(2, n+1):
    # 메모이제이션. d[i]는 i-1이 1이 되기 위해 필요한 연산 + 1
    # 이에따르면
    # d[2] = 1 d[3] = 2 이지만
    # 어차피 아래 나눗셈에서 1로 교체된다.
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) # min 두번째 arg는
                                      # i를 2로 계속 나눴을때의 연산 횟수
        # d[3] = min(d[3], d[1]+1))
        # d[3] = min(2, 1)
        # d[3] = 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
print(d[n])
