import sys

case = int(input())
for i in range(case):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)