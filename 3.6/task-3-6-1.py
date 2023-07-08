countNums = int(input('Количество чисел: '))
countZero = 0

while countNums > 0:
    num = int(input())
    if (num == 0):
        countZero += 1
    countNums -= 1
print("Чисел равных нулю: ", countZero)