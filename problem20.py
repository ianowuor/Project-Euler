#SUM OF DIGITS IN 100 FACTORIAL

import math

x = math.factorial(100)
sum = 0

for digit in str(x):
    sum += int(digit)

print(sum)