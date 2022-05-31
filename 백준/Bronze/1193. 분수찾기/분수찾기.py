N = int(input())
cnt = 0 

while N > sum(range(cnt+1)):
    cnt+=1

last = N-sum(range(cnt))
if N == 1:
    print("1/1")
elif cnt%2==0:
    print(f"{last}/{cnt+1-last}")
else:
    print(f"{cnt+1-last}/{last}")