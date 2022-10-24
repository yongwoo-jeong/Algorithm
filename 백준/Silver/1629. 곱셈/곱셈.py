from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(10**7)

number, mltple, divide = map(int, input().split())

def mlt(number, mltple):
    if mltple == 1:
        return number%divide
    else: 
        tmp = mlt(number,mltple//2)
        if mltple % 2 == 0:
            return tmp*tmp%divide
        else:
            return tmp*tmp*number%divide

answer = mlt(number, mltple)
print(answer)