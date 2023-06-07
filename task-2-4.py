print('Введите стороны прямоугольника:')
a = float(input())
b = float(input())
print('Площадь: ', a*b)
print('Периметр: ', (a+b)*2)

num = 46275
num1 = num % 10
num2 = (num % 100) // 10
num3 = (num % 1000) // 100
num4 = (num % 10000) // 1000
num5 = (num // 10000)
print((num2 ** num1) * num3 / (num5 - num4))