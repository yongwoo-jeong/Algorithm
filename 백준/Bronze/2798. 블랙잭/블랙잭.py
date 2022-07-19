import sys

numbers, N = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
length = len(cards)

def blackjack():
    bigger = 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                total = cards[i]+cards[j]+cards[k]
                if total > N:
                    continue
                else:
                    bigger = max(total, bigger)
    print(bigger)


blackjack()