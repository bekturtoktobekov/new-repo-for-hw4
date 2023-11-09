#списки lists


# students = []
# print(type(students))


# new = list('python')
# print(new)
# students = []

# students = ['GEEKS', 'Bishkek', 312, 996, 5.5, 6.3, True, False]
# print(students)
# print(students[0][-1])

'''add'''

# students_36_3 = ['bektur', 'omurbek', 'erbol', 'akylai', 'malik', 'murat', 'bakai', 'aibek', 'meder']
# for name in students_36_3:
#     print(name.title())
#
# students_36_3_new = [name.title() for name  in students_36_3]
# print(students_36_3_new)
# new_group = ['Tilek', 'Sanjar', 'Diana', 'Aidana']
#
#
# students_36_3_new.append('Nurzada')
# students_36_3_new.insert(0,'Elisei')
# students_36_3_new.insert(6, 'Aziza')
# students_36_3_new.extend(new_group)
# print(students_36_3_new)
# """edit"""
#
# students_36_3_new[0], students_36_3_new[7] = students_36_3_new[7], students_36_3_new[0]
# print(students_36_3_new)
# students_36_3_new[-3] = 'Alisher'
# students_36_3_new.sort(reverse=True)

'''delete'''
# students_36_3_new.clear()
# students_36_3_new.remove('Meder')
# deleted = students_36_3_new.pop(0)
#
# del students_36_3_new[::2]
#
# print(students_36_3_new)
# updated_list = [student for student in students_36_3_new if student not in ['Diana', 'Erbol', 'Alisher', '']]
# print(students_36_3_new)
# print(deleted)
# new_group = ['Tilek', 'Sanjar', 'Diana', 'Aidana']
# new_copy = new_group.copy()
# new_copy = new_group
#
# # new_copy[0] = 'Nikita'
#
# print(new_copy == new_group)
#
# print(new_group)
# print(new_copy)

# print(tuple('python'))
#
# cities = 'Almaty', 'Bishkek', 'Osh', 'Tashkent'
# print(type(cities))
#
# city = ('Tokmok',)
# print(type(city))
#


# expenses = [int(input(f'day expenses: {i}')) for i in range(1, 7+1)]
# print(
#     f'days: {len(expenses)}\n'
#     f'sum exp {sum(expenses)}\n'
#     f"avrg {'%.2f' % (sum(expenses)/len(expenses))}"
# )

# days_expenses = [int(input(f"введите расход дня: {i}")) for i in range(1, 7+1)]
# print(
#     f'дней: {len(days_expenses)}\n'
#     f"сумма расходов {sum(days_expenses)}\n"
#     f"средний расход: {'%.2f' % (sum(days_expenses) / len(days_expenses))}"
# )



