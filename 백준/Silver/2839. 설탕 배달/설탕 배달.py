# 3의 배수 / 5의 배수를 활용해 N 만들기
# 만들수없을경우 -1
# 4 7 11 99 
N = int(input())
five = N // 5
three = N%5 // 3
impossible = (N%5) % 3

if impossible == 0:
  print(five+three)
else:
  if five == 0:
    if N%3 !=0:
      print(-1)
    else:
      print(N//3)
    
  else:
    while five > 0:
      five -=1
      if five == 0:
        if N%3 !=0:
          print(-1)
          break
        else:
          print(N//3)
          break
      else:
        impossible = (N-(5*five)) % 3
        if impossible == 0:
          three = (N-(5*five)) // 3
          print(three+five)
          break
        else:
          pass
  