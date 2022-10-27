from sys import stdin
input = stdin.readline

n = int(input())
mod = 1000000007

def mlt(a,b):
    length = len(a)
    outcome = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            outcome[i][j] = 0
            for x in range(length):
                outcome[i][j] += a[i][x] * b[x][j]
            outcome[i][j] = outcome[i][j] % mod
    return outcome

def power(mat, n):
    if n == 1:
        return mat
    tmp = power(mat,n//2)
    if n%2 == 0:
        return mlt(tmp,tmp)
    else:
        return mlt(mlt(tmp,tmp),mat)

fibbo =[[1,1],[1,0]]
if n <=2:
    print(1)
else:
    print((power(fibbo,n-1)[0][0]))