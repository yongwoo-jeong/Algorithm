from sys import stdin
import re
input = stdin.readline

pmon, q = map(int, input().split())
pmons = {}
for i in range(1, pmon+1):
    pmons[i] = input().strip()

is_numb = re.compile('[0-9]')
reversed_pmons = {v: k for k, v in pmons.items()}
for _ in range(q):
    res = input().strip()
    res_int_valid = is_numb.search(res)
    if res_int_valid:
        print(pmons[int(res)])
    else:
        print(reversed_pmons[res])