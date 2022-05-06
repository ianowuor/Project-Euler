numbers = [0, 1]
i = 0
j = 1
lastNumber = numbers[j]
newNumber = numbers[i] + numbers[j]

while lastNumber < 4000000:
    numbers.append(newNumber)
    i += 1
    j += 1
    newNumber = numbers[i] + numbers[j]
    lastNumber = numbers[j]

sum = 0

for number in numbers:
    if number % 2 == 0:
        sum += number

print(sum)