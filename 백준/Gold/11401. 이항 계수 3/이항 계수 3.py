from sys import stdin
import math
input = stdin.readline

fir, sec = map(int, input().split())
p = 1000000007


def facto(n):
    num = 1
    for i in range(2, n+1):
        num = (num*i) % p
    return num

def power(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    tmp = power(n, k//2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p  

print(facto(fir) * power(facto(sec)*facto(fir-sec),p-2) % p )
