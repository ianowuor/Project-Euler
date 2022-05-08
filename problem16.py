number = 2**1000
sum = 0

for digit in str(number):
    sum += int(digit)

print(sum)