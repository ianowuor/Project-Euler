sum = 0
for i in range(1, 101):
    sum += i

sum = sum * sum
squaresSum = 0

for i in range(1, 101):
    squaresSum += i * i

print(sum - squaresSum)