# SUM OF AMICABLE NUMBERS UPTO 10000

amicable_numbers = []

for a in range(1, 10001):
    divisors_of_a = []
    sum_of_a = 0
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            divisors_of_a.append(i)

    for divisor in divisors_of_a:
        sum_of_a += divisor

    b = sum_of_a
    divisors_of_b = []
    sum_of_b = 0

    for j in range(1, int(b / 2) + 1):
        if b % j == 0:
            divisors_of_b.append(j)

    for divisor in divisors_of_b:
        sum_of_b += divisor

    if sum_of_a == b and sum_of_b == a and a != b:
        if a not in amicable_numbers and b not in amicable_numbers:
            amicable_numbers.append(a)
            amicable_numbers.append(b)


total_sum = 0

for number in amicable_numbers:
    total_sum += number

print(total_sum)


    