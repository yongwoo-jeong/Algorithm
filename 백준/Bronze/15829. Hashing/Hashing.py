import sys


input = sys.stdin.readline
n = int(input())
string = list(input().strip())
thirty_one = [1 for _ in range(n)]
thirty_one = [x*(31**idx) for idx, x in enumerate(thirty_one)]
numbers = [ord(x)-96 for x in string]
answer = list(map(lambda x,y : x*y, thirty_one,numbers))
print(sum(answer)%1234567891)