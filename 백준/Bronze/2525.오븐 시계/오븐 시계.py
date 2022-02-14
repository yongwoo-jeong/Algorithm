hour, minute = map(int, input().split())
cooking = int(input())
cooking_hour = cooking // 60
cooking_min = cooking % 60

if minute + cooking_min == 60:
    hour = hour + cooking_hour + 1
    minute = 0
elif minute + cooking_min > 60:
    hour = hour + cooking_hour + 1
    minute = minute + cooking_min - 60
else:
    hour = hour + cooking_hour
    minute = minute + cooking_min

if hour == 24:
    print(f"0 {minute}")
elif hour > 24:
    print(f"{hour-24} {minute}")
else:
    print(f"{hour} {minute}")