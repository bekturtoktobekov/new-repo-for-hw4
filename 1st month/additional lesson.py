with open('../../results.txt', 'r') as file:
     lines = file.readlines()
     print(lines)
total_rate = 0
num_students = 0
results = {}
for item in lines[1:]:
    name, rate = item.split()[0], item.split()[1]
    results[name] = {"rate": rate}
    total_rate += int(rate)
    num_students +=1

sorted_results = sorted(results.items(), key=lambda y: y[1]['rate'], reverse=True)
print(sorted_results)

print('топ 3 ученика')
for student, (name,results) in enumerate(sorted_results[:3], 1):
    print(f'{student}.name {name} : rate {results["rate"]}')

print(f'средняя оценка студента : {round(total_rate/num_students,1)}')

with open('../../sorted_results1.txt', 'w') as file:
    file.write('sorted_results\n')
    for name , rate in sorted_results:
        file.write(f'name {name} : rate {rate}\n')