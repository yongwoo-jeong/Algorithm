N = int(input())
answer = 1

def fact(N):
  if N == 0:
    print(1)
    return None
  global answer
  answer *=N
  N -=1
  if N == 1:
    print(answer)
  else:
    fact(N)

    
fact(N)