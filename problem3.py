number = 600851475143
primeFactors = []
factor = 2

while number > 1:
    if number % factor == 0:
        while number % factor == 0:
            number = number / factor
            primeFactors.append(factor)
        factor += 1
    else:
        factor += 1

print(primeFactors[len(primeFactors) - 1])

