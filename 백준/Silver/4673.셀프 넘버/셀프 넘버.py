numbers = set(range(1, 10001))
not_self = set()

for n in range(1, 10001):
  for a in str(n):
    n += int(a)
  not_self.add(n)

self_num = sorted(numbers-not_self)

for i in self_num:
  print(i)