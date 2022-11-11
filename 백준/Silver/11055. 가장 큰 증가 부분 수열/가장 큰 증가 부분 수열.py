from sys import stdin
input = stdin.readline

n = int(input())
sqc = list(map(int, input().split()))
dp = [0]*1001

for i in sqc:
    dp[i] = max(dp[:i])+i
print(max(dp))