import sys

input = sys.stdin.readline

x,y,w,h = map(int,input().split())

if x >= w/2:
    x_short = w-x
else:
    x_short = x

if y >= h/2:
    y_short = h-y
else:
    y_short = y 

if x_short >= y_short:
    print(y_short)
else:
    print(x_short)
