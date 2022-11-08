from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
pwd_map = {}
for _ in range(n):
    site, pwd = input().split()
    pwd_map[site] = pwd

for _ in range(m):
    answer = pwd_map[input().strip()]
    print(answer)