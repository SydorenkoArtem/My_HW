cash = int(input('Введите сумму: '))
nominal_1 = 10
nominal_2 = 20
nominal_3 = 50
nominal_4 = 100
nominal_5 = 200
nominal_6 = 500
nominal_7 = 1000
limit = 10
small_nominal = 8800

if cash % nominal_4 == 0 or cash % nominal_5 == 0:
    while cash > small_nominal:
        if cash >= nominal_7:
            print(nominal_7)
            cash = cash - nominal_7
            if cash == 0:
                break
    while cash > 0:
        for i in range(limit):
            if cash >= nominal_1:
                print(nominal_1)
                cash = cash - nominal_1
                if cash == 0:
                    break
        for i in range(limit):
            if cash >= nominal_2:
                print(nominal_2)
                cash = cash - nominal_2
                if cash == 0:
                    break
        for i in range(limit):
            if cash >= nominal_3:
                print(nominal_3)
                cash = cash - nominal_3
                if cash == 0:
                    break
        for i in range(limit):
            if cash >= nominal_4:
                print(nominal_4)
                cash = cash - nominal_4
                if cash == 0:
                    break
        for i in range(limit):
            if cash >= nominal_5:
                print(nominal_5)
                cash = cash - nominal_5
                if cash == 0:
                    break
        for i in range(limit):
            if cash >= nominal_6:
                print(nominal_6)
                cash = cash - nominal_6
                if cash == 0:
                    break
    print('Take your money')
else:
    print("Enter a multiple of:" + str(nominal_4))
