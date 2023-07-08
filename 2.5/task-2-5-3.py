minInvest = int(input('Minimum invest: '))
MikeMoney = int(input('Mike money: '))
IvanMoney = int(input('Ivan money: '))

if (MikeMoney >= minInvest) and (IvanMoney >= minInvest):
    print(2)
elif (MikeMoney >= minInvest) and (IvanMoney < minInvest):
    print('Mike')
elif (IvanMoney >= minInvest) and (MikeMoney < minInvest):
    print('Ivan')
elif (MikeMoney < minInvest) and (IvanMoney < minInvest) and (MikeMoney + IvanMoney >= minInvest):
    print(1)
else:
    print(0)