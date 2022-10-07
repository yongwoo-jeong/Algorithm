import sys

input = sys.stdin.readline

t = int(input().strip())
words = []

for _ in range(t):
    word = input().strip()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=lambda x : len(x))
for i in words:
    print(i)