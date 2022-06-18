import sys

number_list = list(range(10001))
for i in range(2, 101):
  target = i + i
  while target <= 10000:
    if number_list[target] == 0:
      target += i
      continue
    else:
      number_list[target] = 0
      target += i

number_list = [i for i in number_list if i !=0 and i != 1]

T = int(input())

for i in range(T):
  N = int(sys.stdin.readline())
  half = N//2
  
  if half in number_list:
    print(half, half)
  else:
    location = 0
    while half > number_list[location]:
      location += 1
    while True:
      prime_one = number_list[location]
      prime_two = N-prime_one
      if prime_one in number_list and prime_two in number_list:
        break
      else:
        location+=1
    if prime_one < prime_two:
      print(prime_one, prime_two)
    else:
      print(prime_two, prime_one)


