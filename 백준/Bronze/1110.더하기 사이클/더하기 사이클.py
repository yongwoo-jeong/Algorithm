numb = int(input())
init = numb
count = 0 

while True:
    a = numb // 10
    b = numb % 10
    c = (a+b) % 10
    numb = (b*10) + c
    count = count +1
    if numb == init:
        break
print(count)    


