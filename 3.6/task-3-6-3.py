a = int(input('Введите А '))
b = int(input('Ведите B '))

for i in range(a, b + 1):
    if (i % 2 == 0):
        print(i,' ', sep='', end='')