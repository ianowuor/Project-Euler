number = 0
x = 1

while number == 0:
    for i in range(1, 21):
        if x % i == 0:
            if i == 20:
                number = x
                break
            else:
                continue
        else:
            break

    x += 1

print(number)
