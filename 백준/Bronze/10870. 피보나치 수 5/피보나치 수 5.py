N = int(input())
array = [0,1]
# 배열로 붙이면서 N을 깎고 N이 0이 될때 가장 뒤에 있는 수..
# 재귀는 빠져나오는 조건이 있어야함


def fact(N):
  if N == 0:
    print(0)
    return None
  elif N == 1:
    print(1)
    return None
  elif N == 2:
    print(array[-1]+array[-2])
    return None
  else:
    array.append(array[-1]+array[-2])
    fact(N-1)

fact(N)


