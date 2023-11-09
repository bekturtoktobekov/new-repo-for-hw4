'''1) Расширить функцию “Ближайшее Число” из ДЗ № 6'''
def nearest_num(original_list, number):
    sorted_list = sorted(original_list, key=lambda num: abs(number-num))
    return (number, sorted_list)
result = nearest_num(original_list=[5, 20.18, 103, 4], number=27)
print(result)







'''2) Создать функцию для вывода элемента списка/кортежа/строки (iterable) по указанному индексу.'''
# def list_finder(iterable):
#     while True:
#         try:
#             index = int(input('Введите желаемый индекс: '))
#             print(list_iterable[index])
#
#         except IndexError:
#             print(f'Такого индекса нет. Введите от 0 до {len(iterable)-1}')
# list_iterable = 'h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g'
# list_finder(list_iterable)








'''3) Напишите примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение.'''
# temp_celcius = list(map(int,input('введите температуру').split()))
# temp_fahrenheit = list(map(lambda x: x * 9/5 + 32,temp_celcius))
# print(temp_fahrenheit)
#
#
# words = ["apple", "banana", "cherry", "date", "grape"]
# a_filter = list(filter(lambda word: word.startswith('a'),words ))
# print(a_filter)

