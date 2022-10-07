
import sys
import bisect

input = sys.stdin.readline

n = int(input().strip())
numbers = set(map(int,input().split()))

answers = int(input().strip())
cands = list(map(int,input().split()))

for n in cands:
    sys.stdout.write('1\n') if n in numbers else sys.stdout.write('0\n')