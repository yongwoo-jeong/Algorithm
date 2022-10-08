
import sys

input = sys.stdin.readline

time = int(input().strip())
members = []
for _ in range(time):
    member = input().strip()
    members.append(member)


members.sort(key=lambda x: int(x.split()[0]))
for i in members:
    print(i)