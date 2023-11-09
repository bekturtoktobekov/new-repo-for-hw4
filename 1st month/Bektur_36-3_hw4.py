letters = []
numbers = []
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
squared_numbers = [x**2 for x in numbers]
letters[1] = 'G'
letters[7] = 'c'
letters = tuple(letters)
squared_numbers = tuple(squared_numbers)


print(f'кортеж letters: {letters}')
print(f'кортеж numbers: {squared_numbers}')

