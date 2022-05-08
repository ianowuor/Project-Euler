# NUMBER OF SUNDAYS THAT FELL ON THE FIRST OF THE MONTH DURING THE 20TH CENTURY (1 JAN 1901 to 31 DEC 2000)

number_of_Sundays = 0

first_day_index = 2
current_day = 1

for year in range(1901, 2001):
    days = [[], [], [], [], [], [], []]
    for i in range(first_day_index, 7):
        days[i].append(current_day)
        current_day += 1
    
    if year % 4 == 0:
        number_of_days = 366
    else:
        number_of_days = 365

    if number_of_days % 2 == 0:
        first_days = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
    else:
        first_days = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

    while current_day <= number_of_days:
        for day in days:
            day.append(current_day)
            current_day += 1

    number_of_Sundays += len(set(days[0]).intersection(set(first_days)))

    if first_day_index == 6:
        first_day_index = 0
    else:
        first_day_index += 1

    current_day = 1

print(number_of_Sundays)

    


    
