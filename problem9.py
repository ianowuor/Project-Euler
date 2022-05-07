import math

c = 0
found = False
for a in range(1, 999):
    for b in range(1, 999):
        c = 1000 - a - b

        if math.sqrt(a**2 + b**2) == c:
            found = True
            break

    if found:
        break

print(a, b, c)
print(a * b * c)
