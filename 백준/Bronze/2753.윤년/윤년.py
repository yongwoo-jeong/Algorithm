yoon_year = int(input())
if yoon_year % 4 != 0:
    print(0)
else:
    if yoon_year % 100 != 0:
        print(1)
    else:
        if yoon_year % 400 == 0:
            print(1)
        else:
            print(0)