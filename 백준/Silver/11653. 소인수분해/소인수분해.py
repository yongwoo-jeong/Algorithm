N = int(input())
answer_list = []

if N ==1:
  None
else:
  while N>=2:
    for i in range(2,N+1):
      if N%i == 0:
        N = N//i
        answer_list.append(i)
        break
      else:
        pass
  for i in answer_list:
    print(i)