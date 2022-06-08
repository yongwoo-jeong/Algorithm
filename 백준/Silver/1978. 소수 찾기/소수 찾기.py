import sys
total = int(sys.stdin.readline())
number = map(int, sys.stdin.readline().split())
answer = 0

for i in number:
    divisor = []
    if i == 1:
        pass
    elif i == 2:
      answer +=1
    else:
      for j in range(2,i):
        if i%j != 0:
          pass
        else:
          divisor.append(j)
      if divisor == []:
        answer +=1
      else:
        pass
          
print(answer)