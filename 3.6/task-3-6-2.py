num = int(input('Введите число: '))

divisorsCount = 0
div = 1
while div * div < num:
    if num % div == 0:
        divisorsCount += 2
    div += 1
if div * div == num:
    divisorsCount += 1
print(f'Количество натуральных делителей: {divisorsCount}')