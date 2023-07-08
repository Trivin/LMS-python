word = input()

vowels = ['a', 'e', 'i', 'o', 'u']

consonantsCount = 0
vowelsCount = 0

for char in word:
    if char in vowels:
        vowelsCount+=1
    else:
        consonantsCount+=1

print('Число согласных букв в слове = ', consonantsCount)
print('Число гласных букв в слове = ', vowelsCount)