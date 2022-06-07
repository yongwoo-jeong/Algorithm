import sys

times = int(input())

for i in range(times):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    init = list(range(1,15))
    pre = init[0:room]
    next = []
    count = 1 
    answer = 0
    
    while True:
      if count == floor:
        answer = sum(pre)
        break
      for i in range(len(pre)):
        next.append(sum(pre[0:i+1]))
      pre.clear()
      pre +=next
      next.clear()
      count +=1
    print(sum(pre))
  
    #2층 리스트 완성.
