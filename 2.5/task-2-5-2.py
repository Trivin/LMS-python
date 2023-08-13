word = input()

vowels = ['a', 'e', 'i', 'o', 'u']
vowelsCharCount = [0, 0, 0, 0, 0]

consonantsCount = 0
vowelsCount = 0

for char in word:
    if char in vowels:
        vowelsCount+=1
        vowelsCharCount[vowels.index(char)]+=1
    else:
        consonantsCount+=1

print('Число согласных букв в слове = ', consonantsCount)
print('Число гласных букв в слове = ', vowelsCount)

for i in range(0, 4):
   charCount = False
   if vowelsCharCount[i] > 0:
       charCount = vowelsCharCount[i]
   print(f'Число буквы {vowels[i]} в слове = ', charCount)    
