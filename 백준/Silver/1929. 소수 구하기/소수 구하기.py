import math

A,B = map(int, input().split())
number_list = list(range(0,B+1))
root = int(math.sqrt(B))


for i in range(2,root+1):
  if number_list[i] == 0:
    continue
  target = i+i
  try:
    while target <=B:
      number_list[target] = 0
      target+=i
  except:
    continue
  
number_list = number_list[A:]
for i in range(len(number_list)):
  if number_list[i]==0 or number_list[i]==1:
    continue
  else:
    print(number_list[i])