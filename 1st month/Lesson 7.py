#lambda работа с исключениями
#lambda arguments: expression
#map,filter

# from random import choice
# students = [10, 3, 9, 7, 4, 2, 8]
# data = {}
# while students:
#     chosen_student = choice(students)
#     name = input(f'enter name for {chosen_student}:').title
#     try:
#         rate = int(input(f'anter rate for {name}'))
#         if rate not in range(11):
#             print('Mark must be from 0 to 10')
#             continue
#     except:
#         print('only numbers')
#         continue
#     data[name] = rate
#     students.remove(chosen_student)
#     print(students)

numbers = list(range(1,11))
# # print(numbers)
# nums_filtrated = list(filter(lambda num:num%2==0,numbers))
# print(nums_filtrated)

#
# try:
#     print(2 + 'T')
# except:
#     print('error!')
# finally:
#     print('checked')

# expenses = 0
# counter = 7
# while counter > 0:
#     try:
#         day = int(input(f'enter expense: {counter}'))
#     except:
#         print('error!')
#         continue
#     expenses+=day
#     counter-=1
# print(expenses)

mapped_nums = tuple(map(lambda num:num+5,numbers))
print(mapped_nums)
lambda_func = lambda num1, num2: num1 + num2
print(lambda_func(2, 3))
print(type(lambda_func))

#
# def numbers(number1, number2):
#     return number1+number2
# sum_num = numbers(2,3)
# print(sum_num)
#
#
# def show_words(func,words):
#     for i in words:
#         print(func(i))
# show_words(lambda word:word.title(),['team','play'])