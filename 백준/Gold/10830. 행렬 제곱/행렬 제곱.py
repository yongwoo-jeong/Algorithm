import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, p =map(int,input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

def mat_power(mat_one, mat_two):
    new_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new_mat[i][j] += mat_one[i][x]*mat_two[x][j]
                new_mat[i][j] = new_mat[i][j] % 1000
    return new_mat


def power(mat, p):
    if p == 1:
        for i in range(n):
                mat[i] = [x%1000 for x in mat[i]]
        return mat 
    else:
        tmp = power(mat, p//2)
        if p % 2 == 0:
            return mat_power(tmp,tmp)
        else:
            return mat_power(mat_power(tmp,tmp),mat)

answer = power(mat,p)
for i in answer:
    i = [str(x) for x in i]
    print(" ".join(i))