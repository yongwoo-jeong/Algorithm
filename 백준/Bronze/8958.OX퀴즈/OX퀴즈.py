N = int(input())
for a in range(N):
    output = input()
    score = 0
    continuity = 0
    for i in output:
        if i == "O":
            continuity +=1
        elif i == "X":
            continuity = 0
        score += continuity
    print(score)
        