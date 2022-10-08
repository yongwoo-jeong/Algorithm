
import sys

input = sys.stdin.readline

time = int(input().strip())
for _ in range(time):
    vps = input().strip()
    vps =  [x for x in vps]
    bracket = []
    end = len(vps)
    if vps[-1] =='(' or vps[0] ==')':
        print('NO')
    else:
        try:
            while True:
                letter = vps.pop()
                if letter == ')':
                    bracket.append('(')
                else:
                    bracket.pop()
                if vps ==[]:
                    break
        except:
            print("NO")
            continue
        if vps == [] and bracket == []:
            print("YES")
        else:
            print("NO")