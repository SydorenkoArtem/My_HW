cash = int(input())
nominal_1 = 1000
nominal_2 = 500
nominal_3 = 100
nominal_4 = 50
nominal_5 = 1

while cash > 0:
    if cash >= nominal_1:
        print(nominal_1)
        cash = cash - nominal_1
    elif cash >= nominal_2:
        print(nominal_2)
        cash = cash - nominal_2
    elif cash >= nominal_3:
        print(nominal_3)
        cash = cash - nominal_3
    elif cash >= nominal_4:
        print(nominal_4)
        cash = cash - nominal_4
    else:
        print(nominal_5)
        cash = cash - nominal_5
