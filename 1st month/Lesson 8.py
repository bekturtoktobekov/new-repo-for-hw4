'''работа с файлами
# w - write
# a - add
# x - create new file
# r - read'''

# file = open('new file.txt', 'w')
# file.write('слово на кириллице!')
# file.close()


# with open('new file.txt', 'a') as file:
#     file.write('вторая строка')


# with open('new file1.txt','x') as file:
#     file.write('new data!')

# with open('new file.txt', 'r') as file:
#     # print(file.read())
#     print(file.readlines()[-1])


students = [4,1,2,7,3,5,9,13]
with open('../../results.txt', 'w')as new_file:
    new_file.write('36-3 results homework 1-7\n\n')


while students:
    name = input(f'введите имя студента под номером {students[0]}').title()
    rates = input('введите сумму оценок за ДЗ: ')
    with open('../../results.txt', 'a') as file:
        file.write(f'{name} {rates}\n')
    del students[0]
    print(students)