student, prize = map(int, input().split())
scores = list(map(int, input().split()))

print(sorted(scores)[student-prize])
