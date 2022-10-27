import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, c = map(int, input().split())
# IF 3, 7, 7일 경우
answer = 0 
while n!=0:
    n -= 1

    if r < 2**n and c < 2**n:
        answer += (2**n) * (2**n) * 0

    elif r < (2**n) and c >= (2**n) * 1: 
        answer += (2**n) * (2**n) * 1 # 앞 꽉찬 숫자들 카운트해주고
        c -= 2**n # 잘라냈다고 생각

    elif r >= 2**n and c < 2**n:
        answer += (2**n) * (2**n) * 2
        r -= 2**n
    else:
        answer += (2**n) * (2**n) * 3
        c -= 2**n
        r -= 2**n

print(answer)