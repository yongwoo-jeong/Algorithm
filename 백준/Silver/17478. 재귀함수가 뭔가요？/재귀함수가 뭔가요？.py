N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

queue = []
stack = []
times = 0
    
def quote(N):
  global times
  first = "\"재귀함수가 뭔가요?\""
  second = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
  third = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
  fourth = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
  last = "라고 답변하였지."
  queue.append( times*"____" + first)
  queue.append( times*"____" + second)
  queue.append( times*"____" + third)
  queue.append( times*"____" + fourth)
  stack.append( times*"____" + last)
  times +=1
  N -= 1
  if N != 0:
    quote(N)
  else:
    queue.append(times*"____" +"\"재귀함수가 뭔가요?\"")
    queue.append(times*"____" +"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    stack.append( times*"____" +"라고 답변하였지.")

quote(N)

for i in queue:
  print(i)
for i in reversed(stack):
  print(i)
  