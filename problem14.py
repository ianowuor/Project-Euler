# COLLATZ CONJECTUTE
# A number under 1000000 that produces the longest chain

greatest_length = [0, 0]

for i in range(2, 1000001):
    print(i)
    number = i
    chain_length = 1
    while i != 1:
        if i % 2 == 0:
            i /= 2
            chain_length += 1
        else:
            i = (i * 3) + 1
            chain_length += 1

    if chain_length > greatest_length[1]:
        greatest_length[0] = number
        greatest_length[1] = chain_length

print(greatest_length[0], greatest_length[1])
