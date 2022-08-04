N = int(input())
answer_cand = []
init_n = 666


while True:
    if "666" in str(init_n):
        answer_cand.append(init_n)
    if len(answer_cand) == N:
        print(answer_cand[-1])
        break
    init_n += 1
