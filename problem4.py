x = 100
y = 100
palindromes = []

def isPalindrome(z):
    if z < 100000:
        return False
    digits = []
    if z >= 100000:
        diviser = 100000
        while diviser >= 1:
            digits.append(int(z / diviser))
            z -= digits[len(digits) - 1] * diviser
            diviser /= 10
    else:
        diviser = 10000
        while diviser >= 1:
            digits.append(int(z / diviser))
            z -= digits[len(digits) - 1] * diviser
            diviser /= 10

    if digits[0] == digits[5] and digits[1] == digits[4] and digits[2] == digits[3]:
        return True
    else:
        return False

for i in range(x, 1000):
    for j in range(y, 1000):
        number = i * j
        if isPalindrome(number):
            palindromes.append([number, i, j])
        else:
            pass

largest = 0

for palindrome in palindromes:
    if palindrome[0] > largest:
        largest = palindrome[0]

print(largest)