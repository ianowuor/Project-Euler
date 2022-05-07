prime_numbers = [2, 3, 5]
number = 7
sum = 0

def isPrime(a):
    for i in range(3, int(a / 2), 2):
        if a % i == 0:
            return False
        else:
            continue

    return True
            
while prime_numbers[len(prime_numbers) - 1] < 2000000:
    if isPrime(number):
        prime_numbers.append(number)
        print(number)
    number += 2

for prime_number in prime_numbers:
    if prime_number < 2000000:
        sum += prime_number

print(sum)
