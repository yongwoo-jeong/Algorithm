T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    # 호실이 1개일 경우 
    if W == 1:
      print(str(N)+"01")
      continue
    # 1층만 존재하는 경우
    elif H == 1 :
      if N<10:
        print("10"+str(N))
        continue
      else:
        print("1"+str(N))
        continue
        
    remain = N%H
    # 제일 꼭대기 층인 경우
    if remain == 0:
        if N//H<10:
          print(str(H)+"0"+str(N//H))
        else:
          print(str(H)+str(N//H))
    else:
        if N//H<9:
            base = int("10"+str(N//H+1))
        else:
            base = int("1"+str(N//H+1))
        answer = base+100*(remain-1)
        print(answer)
            