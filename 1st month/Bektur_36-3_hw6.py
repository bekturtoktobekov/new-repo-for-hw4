'''Чётное-Нечётноe'''
# def number_check(number):
#     if isinstance(number, int):
#         if number % 2 == 0:
#             return True
#         else:
#             return False
#     else:
#         return None
# result = number_check(3)
# print(result)








'''Правописание'''
# def sentence_check(sentence):
#     if sentence[0].isupper and sentence[-1] == '.':
#         return True
#     else:
#         return False
# new_sentence = input('Введите предложение ')
# result = sentence_check(new_sentence)
# print(result)






'''Калькулятор'''
# def calculator_new(digit_1, sign, digit_2):
#     if sign == '+':
#         result = digit_1 + digit_2
#     elif sign == '-':
#         result = digit_1 - digit_2
#     elif sign == '/':
#         result = digit_1 / digit_2
#         if digit_2 == 0:
#             if digit_2 != 0:
#                 result = digit_1 / digit_2
#             else:
#                 result = "Error: Division by zero"
#     elif sign == '*':
#         result = digit_1 * digit_2
#     return result
# result = calculator_new(digit_1=444, sign='*', digit_2=2332)
# print(result)






'''Ближайшее число'''
def list_number(sequence, number=0):
    difference_list = []
    for i in sequence:
        difference = abs(number - i)
        difference_list.append(difference)
        min_difference = min(difference_list)
        min_index = difference_list.index(min_difference)
        a = sequence[min_index]
    return a
a = list_number([5, 20.18, 103, 4], 27)
print(a)



