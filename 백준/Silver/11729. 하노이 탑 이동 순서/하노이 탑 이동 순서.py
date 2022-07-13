n = int(input())
answer = []

def hanoi(n, start, des, asi):
    if n == 1:
        answer.append(str(start)+" "+str(des))
        return
    hanoi(n-1, start, asi, des)
    answer.append(str(start)+" "+str(des))
    hanoi(n-1, asi, des, start)


hanoi(n, 1, 3, 2)
print(len(answer))
for i in answer:
    print(i)