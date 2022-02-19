import sys

case = int(input())
cnt = 0
for c in range(case):
    word = sys.stdin.readline().strip()
    letter = []
    for w in word:
        if w not in letter:
            letter.append(w)
        elif w in letter:
            if letter[-1] == w:
                letter.append(w)
            else:
                break
    if len(letter) == len(word):
        cnt = cnt + 1
print(cnt)