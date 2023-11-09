day1 = int(input("Enter today's expenses"))
day2 = int(input("Enter today's expenses"))
day3 = int(input("Enter today's expenses"))
day4 = int(input("Enter today's expenses"))
day5 = int(input("Enter today's expenses"))
day6 = int(input("Enter today's expenses"))
day7 = int(input("Enter today's expenses"))

total_expenses = day1+day2+day3+day4+day5+day6+day7
average_week = round(total_expenses/7, 1)
print(f'Total expenses this week: {total_expenses}')
print(f'Average expenses this week: {average_week}')

if total_expenses > 10000:
    print('Потратили много')
elif 3000 <= total_expenses <= 9999:
    print('Потратили средне')
elif 0 < total_expenses <= 2999:
    print('Потратили мало')
else:
    print('Потратили ничего')