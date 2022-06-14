import sys, math

number_list=list(range(0,2*123456+1))
root_number = int(math.sqrt(123456*2))
for i in range(2,root_number+1):
  if number_list[i]==0:
    continue
  target = i+i
  while target <= 2*123456:
    number_list[target] = 0
    target +=i

while True:
  N = int(sys.stdin.readline())
  if N == 0 :
    break
  cnt=0
  new_number = number_list[N+1:2*N+1]
  for i in new_number:
    if i != 0:
      if i == 1:
        pass
      cnt +=1
    
  print(cnt)