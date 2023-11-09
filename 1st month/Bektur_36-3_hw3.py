
consonants = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'
vowels = 'аеёиоуыэюяaeiou'

while True:
    consonants_count = 0
    vowels_count = 0
    letter_count = 0

    word = input('Введите слово: ')
    word1 = word.lower()

    if word == 'стоп':
        break

    for i in word:
        if i in consonants:
            consonants_count += 1
        elif i in vowels:
            vowels_count +=1
        else:
            print('Можно использовать только буквы!')
            break

    for i in word:
        if i.isalpha():
            letter_count += 1

    percentage_consonants = (consonants_count/letter_count)*100
    percentage_vowels = (vowels_count/letter_count)*100
    print(f'Слово: {word}')
    print(f'Количество букв: {letter_count}')
    print(f'Согласные буквы: {consonants_count}')
    print(f'Гласные буквы: {vowels_count}')
    print(f'Согласные:{round(percentage_consonants, 2)}% / Гласные: {round(percentage_vowels, 2)}%')