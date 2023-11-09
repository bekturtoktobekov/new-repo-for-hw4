# функции, аргументы: *args, **kwargs.
# def - define
# DRY
    # определение наименование(параметры):
        # тело функции
        # возвращение результата
    # вызов функции
    # наименование (аргументы)

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat = 'pizza', drink='tea')
# print(monday)

# def plus(*args):
#     return sum(args)
# print(plus(1,2,12,2))

# def get_fullname(name, surname='unknown'): #обязательный позиционный параметр name
#     return f"name: {name},surname: {surname}"
#
# print(get_fullname('Erkin', 'Sotuev'))
# print(get_fullname(surname='Santana',name='Nazarova')) # ключевые аргументы
# print(get_fullname('Diana'))



# def get_square(width: int, lenght: int):
#     '''
#     берет параметр ширины и умножает на длину
#     возвращает площадь прямоугльника
#     '''
#     result = width * lenght
#     return result
# square_2 = get_square(width=5, lenght=8)
# victory_square = get_square(300, 800)
# print(square_2, victory_square, sep='\n')

# students_36_3 = ('Nurzada', 'Bakai', 'Elisei', 'Meder', 'Murat')
# def count_len(sequence):
#     count = 0
#     for _ in students_36_3:
#         count += 1
#     return count
# lenght = count_len(students_36_3)
# print(lenght)

# numbers = [1, 2, 3, 4, 5]
# def count_sum(sequence):
#     count = 0
#     for i in sequence:
#         print(f'{count} + {i} = {count+1}')
#         count += i
#     return count
# count_sum(numbers)

# numbers = [4, 7, 1, 3, 2, 5, 9, 8, 6]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))

# width = 5
# lenght = 8
#
# square_2 = width * lenght
#
# print(square_2)
#
# width = 300
# lenght = 800
# square_victory = width * lenght
# print(square_victory)


