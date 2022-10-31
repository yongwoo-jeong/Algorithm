from sys import stdin
input = stdin.readline

computers = int(input())
pairs = int(input())
pair_net = {x: [] for x in range(1, computers+1)}

for _ in range(pairs):
    start, end = map(int, input().split())
    pair_net[start].append(end)
    pair_net[end].append(start)

stack = []
stack.append(1)
warmed = []

while stack:
    top = stack.pop()
    if top in warmed:
        continue
    warmed.append(top)
    if top in pair_net.keys():
        for i in pair_net[top]:
            stack.append(i)

warmed = set(warmed)
warmed.remove(1)
print(len(warmed))