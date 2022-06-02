import math

up, down, tree = map(int, input().split())

print(math.ceil((tree-up)/(up-down))+1)
    
