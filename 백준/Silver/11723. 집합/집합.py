from sys import stdin
input = stdin.readline

n = int(input())
sets = set()
for _ in range(n):
    input_string = input().split()
    if input_string[0] == "all":
        sets = set([x for x in range(1, 21)])
    elif input_string[0] == "empty":
        sets = set()
    else:
        transaction, numb = input_string[0], int(input_string[1])
        if transaction == "add":
            sets.add(numb)
        elif transaction == "remove":
            try:
                sets.remove(numb)
            except:
                pass
        elif transaction == "check":
            if numb in sets:
                print(1)
            else:
                print(0)
        else:
            if numb in sets:
                sets.remove(numb)
            else:
                sets.add(numb)

