"""
# Integer to Roman number system conversion up to 1999
numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
"""


def solution1(value):
    lookupTable = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['M']
    ]
    number_list = list(str(value))
    result = ''
    for i in range(0, len(number_list)):
        number = int(number_list.pop())
        if number != 0:
            character = lookupTable[i][int(number) - 1]
            result = character + result

    return result


def solution2(value):
    romanSymbols = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M']
    ]
    number_list = list(str(value))
    result = ''
    for i in range(0, len(number_list)):
        number = int(number_list.pop())
        # Numeric system rules up to 1999
        if 0 < number <= 3:
            current = romanSymbols[i][0] * number
        elif number == 4:
            current = romanSymbols[i][0] + romanSymbols[i][1]
        elif number == 5:
            current = romanSymbols[i][1]
        elif 5 < number <= 8:
            current = romanSymbols[i][1] + romanSymbols[i][0] * number
        elif number == 9:
            current = romanSymbols[i][0] + romanSymbols[i + 1][0]
        result = current + result

    return result


print(solution1(1111), solution1(1999))
print(solution2(1111), solution1(1999))
