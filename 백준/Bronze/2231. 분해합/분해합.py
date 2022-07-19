import sys

N = int(sys.stdin.readline().strip())

# 애초에 등록할때 dict형태로?
collec = {}
for i in range(1, 1000000):
    tmp = i
    acc = i
    while i != 0:
        acc += i % 10
        i = i//10
    collec[tmp] = acc

collec_keys = list(collec.keys())
collec_values = list(collec.values())
if N in collec_values:
    index_list = collec_values.index(N)
    print(collec_keys[index_list])
else:
    print(0)