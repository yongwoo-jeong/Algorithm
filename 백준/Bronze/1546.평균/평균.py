N = int(input())
score = list(map(int, input().split()))
high = max(score)
new_score = []
for i in score:
    new_score.append(i/high*100)
avg = sum(new_score) / len(new_score)
print(avg)
    