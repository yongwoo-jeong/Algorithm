fix, var, prc = map(int,input().split())
amt = 0
if var >= prc:
    amt = -1
else:
    amt = ((fix+var-prc)//(prc-var)) +2
print(amt)