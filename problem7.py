prime_numbers = [2, 3, 5]
number = 7

def isPrime(a):
    for i in range(3, int(a / 2), 2):
        if a % i == 0:
            return False
        else:
            continue

    return True
            
while len(prime_numbers) < 10001:
    if isPrime(number):
        prime_numbers.append(number)
    number += 2

print(prime_numbers[len(prime_numbers) - 1])

    