n = list(map(int,input().split()))
n = [i**2 for i in n]
print(sum(n)%10)