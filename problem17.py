# THE TOTAL NUMBER OF CHARACTERS FOR NUMBERS FROM 1 TO 100 EXCLUDING SPACES AND HYPHENS

word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word_numbers2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
other_words = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def digits_to_100(words, words1, words2):
    number_of_digits = 0
    for word in words:
        number_of_digits += len(word)

    for word in words1:
        number_of_digits += len(word)

    for i in range(8):
        base_string = words2[i]
        for j in range(10):
            if j == 0:
                number_of_digits += len(base_string)
            else:
                number_of_digits += len(base_string + words[j - 1])

    return number_of_digits


def digits_to_1000(base_digits, words):
    number_of_digits = base_digits
    number_of_digits += base_digits * 9
    for i in range(9):
        number_of_digits += len(words[i] + "hundred")
        number_of_digits += len(words[i] + "hundredand") * 99

    number_of_digits += len("onethousand")
    return(number_of_digits)

print(digits_to_1000(digits_to_100(word_numbers, word_numbers2, other_words), word_numbers))
