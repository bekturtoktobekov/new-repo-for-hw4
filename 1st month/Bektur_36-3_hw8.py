file = open('../../results.txt', 'r')
text = file.readlines()
total_marks = 0
students_marks = {}
print('  ALL STUDENTS:')
for i in text[1:]:
    name, mark = i.strip().split()
    students_marks[name] = f'mark {mark}'
    total_marks += int(mark)
for name, mark in students_marks.items():
    print(f'{name} : {mark}')

sorted = sorted(students_marks.items(), key=lambda x:x[1], reverse=True)
top3 = sorted[:3]
print('  THE BEST 3 STUDENTS:')
for name, mark in enumerate(top3[:3], 1):
    print(f'{name} : {mark}')

average_mark = total_marks/len(students_marks)
print(f'  AVERAGE MARK: {average_mark}')

with open('../../sorted_results.txt', 'w') as file:
    file.write('Total students list\n')
    for name, mark in sorted:
        file.write(f'{name}: {mark}\n')

    file.write('THE BEST 3 STUDENTS:\n')
    for name, mark in enumerate(top3 ,1):
        file.write(f'{name}: {mark}\n')

    file.write(f'AVERAGE MARK: {average_mark}\n')


